import logging
from typing import Optional, Dict
from mongoengine.errors import DoesNotExist, ValidationError
from .models import Article

logger = logging.getLogger(__name__)


def create_article(article_info) -> Optional[Article]:
    try:
        article = Article.objects.get(url=article_info.get("url"))
        return article
    except DoesNotExist as e:
        pass
    try:
        article = Article(**article_info).save()
        return article
    except ValidationError as e:
        logger.error(e)
        return None


def update_article(article_id: str, doc: Dict) -> bool:
    try:
        Article.objects(id=article_id).update(**doc)
    except Exception as e:
        logger.error(e)
        return False
    return True
