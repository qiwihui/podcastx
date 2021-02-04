import json
import logging
import marshmallow
from flask_restful import Resource, request
from flask_jwt_extended import get_jwt_identity, jwt_optional
from mongoengine.queryset import Q
from database.models import Article as ArticleDoc, User
from resources.utils import get_object
from resources.schema import ArticleSearchSchema


logger = logging.getLogger(__name__)


class ExploreArticles(Resource):

    @jwt_optional
    def get(self):
        user_id = get_jwt_identity()
        user = None
        if user_id:
            user = get_object(User, user_id)
        
        schema = ArticleSearchSchema()
        try:
            validated_data = schema.load(request.args)
        except marshmallow.exceptions.ValidationError as error:
            message = "请求错误"
            for msg in error.messages.values():
                message = msg[0]
            resp = {"status": 0, "msg": message, "errors": error.messages}
            return resp, 500

        page = validated_data.get("page", 0)
        per_page = validated_data.get("per_page", 10)
        search = validated_data.get("search", None)
        article_docs = ArticleDoc.objects()
        if search:
            article_docs = article_docs.filter(Q(title__icontains=search)|Q(content__icontains=search))
        article_docs = article_docs.order_by('-created_at')
        articles = [
            article.json(user)
            for article in article_docs[page * per_page : (page + 1) * per_page]
        ]
        return {
            "status": 1,
            "msg": "ok",
            "data": {"articles": articles},
        }, 200
