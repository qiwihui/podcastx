import json
import logging
import marshmallow
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models import Article as ArticleModel, User
from database.utils import create_article, update_article
from resources.schema import ArticleUrlSchema, ArticleActionSchema
from resources.utils import get_object
from tasks import task_fetch_url


logger = logging.getLogger(__name__)


class Article(Resource):
    def get(self, article_id):
        article = get_object(ArticleModel, article_id)
        if article:
            data = json.loads(article.to_json())
            data["likes_count"] = article.likes_count
            data["content"] = data["content"][:100] if data["content"] else ""
            data["audios"] = [f"/media/{article.id}/full.mp3"] if article.status == 1 else []
        else:
            data = {}

        result = {"status": 1, "msg": "ok", "data": data}
        return result, 200

    @jwt_required
    def post(self, article_id):
        data = request.get_json()

        schema = ArticleActionSchema(unknown="EXCLUDE")
        try:
            validated_data = schema.load(data)
        except marshmallow.exceptions.ValidationError as error:
            message = "请求错误"
            for msg in error.messages.values():
                message = msg[0]
            resp = {"status": 0, "msg": message, "errors": error.messages}
            return resp, 200

        article = get_object(ArticleModel, article_id)
        if article:
            user_id = get_jwt_identity()
            user = get_object(User, user_id)
            action = validated_data.get("action")
            if action == "unlike":
                article.update(pull__likes=user)
            elif action == "like":
                article.update(add_to_set__likes=[user])
            article = get_object(ArticleModel, article_id)
            result = {"status": 1, "msg": "ok", "data": {"likes_count": len(article.likes)}}
            return result, 200
        else:
            result = {"status": 0, "msg": "error"}
            return result, 404

    @jwt_required
    def delete(self, article_id):
        user_id = get_jwt_identity()
        user = get_object(User, user_id)
        article = get_object(ArticleModel, article_id)
        if article:
            user.update(pull__articles=article)

        result = {"status": 1, "msg": "ok"}
        return result, 200


class UserArticles(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        user = get_object(User, user_id)
        page = int(request.args.get("page", 0))
        per_page = int(request.args.get("per_page", 10))
        articles = [
            {
                **json.loads(article.to_json()),
                "likes_count": article.likes_count,
                "content": article.content[:100] if article.content else "",
                "like": 1 if article.check_like(user) else 0,
            }
            for article in user.articles[page * per_page : (page + 1) * per_page]
        ]

        return {
            "status": 1,
            "msg": "ok",
            "data": {"articles": articles},
        }, 200

    @jwt_required
    def post(self):
        data = request.get_json()
        schema = ArticleUrlSchema()
        try:
            validated_data = schema.load(data)
        except marshmallow.exceptions.ValidationError as error:
            message = "请求错误"
            for msg in error.messages.values():
                message = msg[0]
            resp = {"status": 0, "msg": message, "errors": error.messages}
            return resp, 500
        url = validated_data.get("url")
        ap = create_article({"url": url})
        # add article to user
        user_id = get_jwt_identity()
        if user_id:
            user = get_object(User, user_id)
            user.update(add_to_set__articles=[ap])
        if ap.status == 0:
            task_fetch_url.delay(str(ap.id))
        return {
            "status": 1,
            "msg": "ok",
            "data": {"id": str(ap.id)},
        }, 200


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
