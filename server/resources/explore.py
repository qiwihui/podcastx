import json
import logging
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models import Article as ArticleDoc, User
from resources.utils import get_object


logger = logging.getLogger(__name__)


class ExploreArticles(Resource):

    def get(self):
        user_id = get_jwt_identity()
        user = None
        if user_id:
            user = get_object(User, user_id)
        page = int(request.args.get("page", 0))
        per_page = int(request.args.get("per_page", 10))
        
        article_docs = ArticleDoc.objects.order_by('-created_at')
        articles = [
            article.json(user)
            for article in article_docs[page * per_page : (page + 1) * per_page]
        ]
        return {
            "status": 1,
            "msg": "ok",
            "data": {"articles": articles},
        }, 200
