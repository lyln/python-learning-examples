__author__ = 'ljd'
from flask_sqlalchemy import SQLAlchemy
from wechat_flask import app
import config

# basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
