# coding: utf-8
from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
# from config import BaseConfig
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


ma = Marshmallow()
db = MongoEngine()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(BaseConfig):

    app = Flask(__name__)
    app.config.from_object(BaseConfig)

    # NOTE: This fixes "UserWarning: MongoClient opened before fork."
    # I'm not aware of side effects yet. Default value is/was "True"
    app.config['MONGODB_CONNECT'] = False

    ma.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    return app


def add_api_support(app):

    api = Api(app)

    from resources.routes import initialize_routes
    initialize_routes(api)

    return app
