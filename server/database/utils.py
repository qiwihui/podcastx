import logging
from typing import Optional, Dict
from mongoengine.errors import DoesNotExist, ValidationError
from .models import Article, User, UserArticle

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


def user_add_article(user: User, article: Article) -> Optional[UserArticle]:

    ua = UserArticle.objects(user=user, article=article)
    if not ua:
        try:
            ua = UserArticle(user=user, article=article).save()
        except ValidationError as e:
            logger.error(e)
            return None
    return ua


def user_delete_article(user: User, article: Article) -> bool:
    try:
        UserArticle.objects(user=user, article=article).delete()
    except Exception as e:
        logger.error(e)
        return False
    return True
