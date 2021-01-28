from pathlib import Path
from celery.utils.log import get_task_logger
from mongoengine.errors import DoesNotExist
from factory import celery_app
from config import BaseConfig
from ut import url2article
from converter import make_audios, make_segments
from database.models import Article


logger = get_task_logger(__name__)


@celery_app.task(name="tasks.task_fetch_url")
def task_fetch_url(article_id: str, url: str):
    try:
        article = Article.objects.get(id=article_id)
    except DoesNotExist as e:
        return
    if article.status == 1:
        return
    art = url2article(url)

    segs = make_segments(art.cleaned_text)
    article.chuncks = segs
    article.domain = art.domain
    article.content = art.cleaned_text
    article.title = art.title
    article.save()
    
    folder = Path(BaseConfig.MEDIA_ROOT) / f"{article_id}"
    if not folder.exists():
        folder.mkdir(parents=True)
    # make audios
    make_audios(segs, str(folder))

    article.status = 1
    article.save()
