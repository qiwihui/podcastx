import json
import logging
import marshmallow
from flask import jsonify
from mongoengine.errors import DoesNotExist
from flask_restful import Resource, request
from database.models import Article as ArticleModel
from database.utils import create_article, update_article
from tasks import task_fetch_url
from resources.schema import ArticleUrlSchema

logger = logging.getLogger(__name__)


def get_object(model, id):
    try:
        target = model.objects.get(id=id)
    except DoesNotExist as e:
        logger.error(e, exc_info=True)
        target = None
    return target


class Article(Resource):

    def get(self, article_id):
        article = get_object(ArticleModel, article_id)
        if article:
            data = json.loads(article.to_json())
        else:
            data = {}

        result = {"status": 1, "msg": "ok", "data": data}
        return result, 200

    def delete(self, article_id):
        article = get_object(ArticleModel, article_id)
        if article:
            article.delete()

        result = {"status": 1, "msg": "ok"}
        return result, 200


class Articles(Resource):
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

        task_fetch_url.delay(str(ap.id))
        return {
            "status": 1,
            "msg": "ok",
            "data": {"id": str(ap.id)},
        }, 201


class ArticleAudios(Resource):

    def get(self, article_id):
        article = get_object(ArticleModel, article_id)
        if article:
            return {
                "status": 1,
                "msg": "ok",
                "data": {
                    "title": article.title,
                    "author": article.author,
                    "audios": [f"/media/{article.id}/{part}.mp3" for part in len(article.chuncks)]
                },
            }, 200
        else:
            return {
                "status": 0,
                "msg": "article not found",
                "data": {},
            }, 400
