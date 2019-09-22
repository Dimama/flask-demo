from flask import Flask, current_app
from flask_restful import Api

from api.resources import Stub
from db_wrapper import DBWrapper

from config import DB_HOST, DB_PORT, DB_PASSWORD, DB_USER, DATABASE


def create_app():
    app = Flask(__name__)

    with app.app_context():
        current_app.db_wrapper = DBWrapper(DB_HOST, DB_PORT, DATABASE, DB_USER, DB_PASSWORD)

    api = Api(app)
    api.add_resource(Stub, '/stub')
    return app
