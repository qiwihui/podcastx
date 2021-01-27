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


class Article(Resource):
    def get_object(self, id):
        try:
            article = ArticleModel.objects(id=id)
        except DoesNotExist as e:
            logger.error(e, exc_info=True)
            article = None
        return article

    def get(self, article_id):
        article = self.get_object(article_id)
        if article:
            data = json.loads(article.as_json())
        else:
            data = {}

        result = {"status": 1, "msg": "ok", "data": data}
        return result, 200

    def delete(self, article_id):
        article = self.get_object(article_id)
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
        import pdb

        pdb.set_trace()
        url = validated_data.get("url")
        ap = create_article({"url": url})

        task_fetch_url(url)
        return {}, 201


class ArticlePodcast(Resource):
    def get(self, article_id):
        part = request.args.get("p", 0)
        return {}, 200
