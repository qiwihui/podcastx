import datetime
import marshmallow
from flask import request
from database.models import User
from flask_restful import Resource
from resources.schema import RegisterSchema, LoginSchema
from resources.utils import get_object
from flask_jwt_extended import create_access_token
from mongoengine.queryset import Q


class Register(Resource):
    """注册"""

    def post(self):
        data = request.get_json()
        schema = RegisterSchema()
        try:
            validated_data = schema.load(data)
        except marshmallow.exceptions.ValidationError as error:
            message = "请求错误"
            for msg in error.messages.values():
                message = msg[0]
            resp = {"status": 0, "msg": message, "errors": error.messages}
            return resp, 200

        user = User(**validated_data)
        user.hash_password()
        user.save()
        id = user.id
        return {
            "status": 1,
            "msg": "ok",
            "data": {"id": str(id)},
        }, 200


class Login(Resource):
    def post(self):
        data = request.get_json()
        schema = LoginSchema(unknown='EXCLUDE')
        try:
            validated_data = schema.load(data)
        except marshmallow.exceptions.ValidationError as error:
            message = "请求错误"
            for msg in error.messages.values():
                message = msg[0]
            resp = {"status": 0, "msg": message, "errors": error.messages}
            return resp, 200

        user = User.objects.get(Q(email=validated_data.get("username")) | Q(username=validated_data.get("username")))
        authorized = user.check_password(validated_data.get("password"))
        if not authorized:
            return {
                "status": 0,
                "msg": "用户名、邮箱或者密码错误",
                "error": "Email or password invalid",
            }, 200

        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return {"status": 1, "msg": "ok", "token": access_token}, 200
