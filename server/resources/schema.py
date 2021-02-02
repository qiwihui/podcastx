from app import ma
from marshmallow import fields, validates, validate, ValidationError
from resources.utils import get_object, error_messages
from database.models import User


class ArticleUrlSchema(ma.Schema):

    url = fields.URL(required=True)


class RegisterSchema(ma.Schema):

    email = fields.Email(required=True, error_messages=error_messages("邮箱"))
    password = fields.String(required=True, validate=validate.Length(min=6), error_messages=error_messages("密码"))
    username = fields.String(required=True, error_messages=error_messages("用户名"))

    @validates("email")
    def validate_email(self, value):
        if get_object(User, value, "email"):
            raise ValidationError("邮箱已经存在")

    @validates("username")
    def validate_username(self, value):
        if get_object(User, value, "username"):
            raise ValidationError("用户名已经存在")


class LoginSchema(ma.Schema):

    password = fields.String(required=True, validate=validate.Length(min=6), error_messages=error_messages("密码"))
    username = fields.String(required=True, error_messages=error_messages("邮箱或用户名"))

    @validates("username")
    def validate_username(self, value):
        if not get_object(User, value, "username") and not get_object(User, value, "email"):
            raise ValidationError("用户不存在存在")


class ArticleActionSchema(ma.Schema):

    action = fields.String(
        required=True, validate=validate.OneOf(["like", "unlike"]), error_messages=error_messages("操作")
    )
