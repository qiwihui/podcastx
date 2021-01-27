import celery
import redis
from app import celery
from config import BaseConfig
from celery.utils.log import get_task_logger
from ut import url2text
from converter import make_audios

logger = get_task_logger(__name__)


@celery.task(name='tasks.task_fetch_url')
def task_fetch_url(url):
    logger.debug("Alreading ran")
    text = url2text(url)
    make_audios(text)
    return True
