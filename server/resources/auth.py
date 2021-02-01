import marshmallow
from flask import request
from database.models import User
from flask_restful import Resource
from resources.schema import RegisterSchema
from resources.utils import get_object


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
