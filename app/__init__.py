#!/usr/bin/env python
# encoding: utf-8
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import config
import os

app = Flask(__name__)

db = SQLAlchemy()

with app.app_context():
    config_name = os.getenv('CONFIG') or 'default'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)


import models
