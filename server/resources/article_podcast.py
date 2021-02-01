import json
import logging
import marshmallow
from flask import jsonify
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from mongoengine.errors import DoesNotExist
from database.models import Article as ArticleModel, User
from database.utils import create_article, update_article
from resources.schema import ArticleUrlSchema
from resources.utils import get_object
from tasks import task_fetch_url


logger = logging.getLogger(__name__)


class Article(Resource):
    def get(self, article_id):
        article = get_object(ArticleModel, article_id)
        if article:
            data = json.loads(article.to_json())
            data["audios"] = (
                # [f"/media/{article.id}/{part}.mp3" for part in range(len(article.chuncks))] if article.status == 1 else []
                [f"/media/{article.id}/full.mp3"]
                if article.status == 1
                else []
            )
        else:
            data = {}

        result = {"status": 1, "msg": "ok", "data": data}
        return result, 200

    @jwt_required
    def delete(self, article_id):
        article = get_object(ArticleModel, article_id)
        if article:
            article.delete()

        result = {"status": 1, "msg": "ok"}
        return result, 200


class Articles(Resource):

    # @jwt_required
    def post(self):
        data = request.get_json()
        schema = ArticleUrlSchema()
        try:
            validated_data = schema.load(data)
        except marshmallow.exceptions.ValidationError as error:
            resp = {"status": 0, "msg": "error", "errors": error.messages}
            return resp, 500
        url = validated_data.get("url")
        ap = create_article({"url": url})
        # add article to user
        user_id = get_jwt_identity()
        if user_id:
            user = get_object(User, user_id)
            if user:
                user.update(add_to_set__articles=[ap])
        if ap.status == 0:
            task_fetch_url.delay(str(ap.id))
        return {
            "status": 1,
            "msg": "ok",
            "data": {"id": str(ap.id)},
        }, 200


class ArticleAudios(Resource):
    def get(self, article_id):
        article = get_object(ArticleModel, article_id)
        if article:
            return {
                "status": 1,
                "msg": "ok",
                "data": {"audios": [f"/media/{article.id}/{part}.mp3" for part in range(len(article.chuncks))]},
            }, 200
        else:
            return {
                "status": 0,
                "msg": "article not found",
                "data": {},
            }, 400
