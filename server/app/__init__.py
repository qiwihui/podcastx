# coding: utf-8
from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
# from config import BaseConfig
from flask_mongoengine import MongoEngine


ma = Marshmallow()
db = MongoEngine()


def create_app(BaseConfig):

    app = Flask(__name__)
    app.config.from_object(BaseConfig)

    ma.init_app(app)
    db.init_app(app)

    return app


def add_api_support(app):

    api = Api(app)
    # celery_app = create_celery_app(app)
    # ma = Marshmallow(app)

    # from database.db import initialize_db
    # initialize_db(app)

    from resources.routes import initialize_routes
    initialize_routes(api)

    return app
