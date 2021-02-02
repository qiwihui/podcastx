import datetime
from app import db
from flask_bcrypt import generate_password_hash, check_password_hash
import mongoengine_goodjson as gj


class Article(gj.Document):

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
    status = db.IntField(default=0, min_value=0, max_value=3)

    meta = {
        "collection": "article",
        "indexes": [
            "url",
            "$url",  # text index
            "#url",  # hashed index
        ],
    }


class User(gj.Document):

    username = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)

    articles = db.ListField(db.ReferenceField(Article), default=list)

    meta = {
        "collection": "user"
    }

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode("utf8")

    def check_password(self, password):
        return check_password_hash(self.password, password)
