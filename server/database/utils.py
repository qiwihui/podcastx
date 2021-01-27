import logging
from typing import Optional, Dict
from .models import Article

logger = logging.getLogger(__name__)


def create_article(article_info) -> Optional[Article]:
    try:
        article = Article(**article_info).save()
        return article
    except Exception as e:
        logger.error(e)
        return None


def update_article(article_id: int, doc: Dict) -> bool:
    try:
        Article.objects(id=article_id).update(**Dict)
    except Exception as e:
        logger.error(e)
        return False
    return True
