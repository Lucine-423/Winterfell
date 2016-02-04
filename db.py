#cat db.py
from flask import Flask
import os
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s/%s' % (
        os.environ.get('DATABASE_USERNAME', 'root'),
        os.environ.get('DATABASE_PASSWORD', 'BIG BEN'),
        os.environ.get('DATABASE_HOST', 'localhost'),
        os.environ.get('DATABASE_DB', 'Winterfell'),
    )
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

class User(db.Model):
    user_id = db.Column(db.Integer,primary_key = True)
    user_name = db.Column(db.String(64),nullable=False)
    user_nikename = db.Column(db.String(64),nullable=False)
    user_email = db.Column(db.String(64),nullable=False)
    user_pass = db.Column(db.String(64),nullable=False)

    def __init__(self,user_name,user_nikename,user_email,user_pass):
        self.user_name = user_name
        self.user_nikename = user_nikename
        self.user_email = user_email
        self.user_pass = user_pass
