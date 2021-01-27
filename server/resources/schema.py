from app import ma
from marshmallow import fields


class ArticleUrlSchema(ma.Schema):

    url = fields.URL(required=True)
