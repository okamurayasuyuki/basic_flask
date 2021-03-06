#coding: utf-8


import os
import sys
#正しくmodelsを読み込む
sys.path.append(os.getcwd())
from flask import Flask
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from basic_app import config
global db
db = SQLAlchemy()
def load_models():
    from basic_app.users import models
    from basic_app.videos import models

load_models()

def init_extensions(app):
    db.init_app(app)


def init_views(app):
    from basic_app import users
    from basic_app import videos
    app.register_blueprint(users.bp, url_prefix="/")
    app.register_blueprint(videos.bp,url_prefix="/videos")


def create_app(config=config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.secret_key = 'tekitouna himitu no kagi'
    init_extensions(app)
    init_views(app)
    return app

