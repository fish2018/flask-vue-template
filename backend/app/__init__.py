from flask import Flask
from .models import db
from .api import api
from .marshalling import ma
from flask_cors import CORS
from app.utils import log

cors = CORS()

def register_plugin(app):
    api.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)
    log.init_app(app)

    with app.app_context():
        # db.drop_all()
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.APP_ENV')
    register_plugin(app)
    return app