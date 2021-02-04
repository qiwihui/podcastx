import json
import datetime
from dateutil import parser
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
    def likes_count(self) -> int:
        return len(self.likes) if self.likes else 0

    def check_like(self, user) -> bool:
        return user and user in self.likes

    def json(self, user=None):

        data = {
            **json.loads(self.to_json()),
            "likes_count": self.likes_count,
            "content": self.content[:100] if self.content else "",
            "like": 1 if user and self.check_like(user) else 0,
            "audios": [f"/media/{self.id}/full.mp3"] if self.status == 1 else [],
            # check if user already added article
            "added": 1 if user and self.check_added(user) else 0,
        }

        return data
    
    def check_added(self, user) -> bool:

        ua = UserArticle.objects.find(user=user, article=self)
        return 1 if ua else 0


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
