import datetime
from .db import db


# class User(db.EmbeddedDocument):

#     username = db.StringField(required=True)
#     email = db.EmailField(required=True)


class Article(db.Document):

    url = db.URLField()
    author = db.StringField(default="")
    chuncks = db.ListField(db.StringField(), default=list)
    content = db.StringField(default="")
    domain = db.StringField(default="")
    title = db.StringField(default="")
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.datetime.utcnow)
    image = db.URLField(required=False)
    # owner = None

    meta = {
        "collection": "article",
        "indexes": [
            "url",
            "$url",  # text index
            "#url",  # hashed index
        ],
    }
