# -*- coding: utf-8 -*-
__author__ = 'ljd'
from flask import Flask

from wechat_flask.auth import auth,login_manager



app = Flask(__name__)
app.config.from_object('config')

from . import views
from .auth.views import auth

#flask-blueprint register
app.register_blueprint(auth,url_prefix='/auth')


# flask-login setting
app.secret_key = 'wechatpy'
# 初始化flash-login
login_manager.init_app(app)



