import os


class BaseConfig(object):
    SECRET_KEY = os.getenv("SECRET_KEY", None)
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", None)
    DEBUG = os.getenv("DEBUG", False)
    # redis
    REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
    REDIS_PORT = os.getenv("REDIS_PORT", 6379)
    REDIS_DB = os.getenv("REDIS_DB", 1)
    # Celery.
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}")
    CELERY_RESULT_BACKEND = CELERY_BROKER_URL
    CELERY_ACCEPT_CONTENT = ["json"]
    CELERY_TASK_SERIALIZER = "json"
    CELERY_RESULT_SERIALIZER = "json"
    CELERY_REDIS_MAX_CONNECTIONS = 5
    # save audio file
    MEDIA_ROOT = os.getenv("MEDIA_ROOT", "/data/podcastx/media/")

    MONGODB_SETTINGS = {
        'db': os.getenv("MONGO_INITDB_DATABASE", "podcastx"),
        'host': os.getenv('MONGO_URI', 'mongodb://mongodb:27017/podcastx')
    }
