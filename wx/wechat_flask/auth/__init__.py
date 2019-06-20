# -*- coding: utf-8 -*-
# @Time    : 2017/10/25 下午8:29
# @Author  : lyln

from flask import Blueprint
from flask_login import LoginManager


auth = Blueprint('auth', __name__,template_folder='templates',static_folder='static')


# flask-login setting
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.login_message = '请先登陆'



