# coding: utf-8
from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
from config import BaseConfig
from factory import create_celery_app


app = Flask(__name__)
app.config.from_object(BaseConfig)

api = Api(app)
celery_app = create_celery_app(app)
ma = Marshmallow(app)

from database.db import initialize_db
initialize_db(app)

from resources.routes import initialize_routes
initialize_routes(api)
