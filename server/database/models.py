import datetime
from app import db
from flask_bcrypt import generate_password_hash, check_password_hash
import mongoengine_goodjson as gj


class Article(gj.Document, db.Document):

    url = db.URLField()
    author = db.StringField(default="")
    chuncks = db.ListField(db.StringField(), default=list, exclude_to_json=True)
    content = db.StringField(default="")
    domain = db.StringField(default="")
    title = db.StringField(default="")
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.datetime.utcnow)
    image = db.URLField(required=False)
    # owner = None
    status = db.IntField(default=0, min_value=0, max_value=3)
    likes = db.ListField(db.ReferenceField("User"), default=list, exclude_to_json=True)

    meta = {
        "collection": "article",
        "indexes": [
            "url",
            "$url",  # text index
            "#url",  # hashed index
        ],
        "strict": False,
    }

    @property
    def likes_count(self):
        return len(self.likes) if self.likes else 0

    def check_like(self, user):
        return user in self.likes


class User(gj.Document, db.Document):

    username = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)

    meta = {
        "collection": "user",
        "strict": False,
    }

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode("utf8")

    def check_password(self, password):
        return check_password_hash(self.password, password)


class UserArticle(gj.Document, db.Document):

    user = db.ReferenceField(User)
    article = db.ReferenceField(Article)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)

    meta = {
        "collection": "user_article",
        "strict": False,
    }
