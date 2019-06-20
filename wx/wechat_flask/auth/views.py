# -*- coding: utf-8 -*-
# @Time    : 2017/10/25 下午8:29
# @Author  : lyln

import urllib2,json
from flask import render_template,abort,request,flash,session,redirect,url_for

from wechat_flask.auth import auth
from flask_login import login_required,login_user,logout_user

from ..models import User
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

# test method
@auth.route('/test')
@login_required
def test():
    return "yes , you are allowed"

@auth.route('/login',methods=["GET","POST"])
def login():
    # get mafengwo background
    # url = "https://passport.mafengwo.cn/api.php/relationInfo"
    # req = urllib2.Request(url)
    # req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.75 Safari/537.36')
    # res = urllib2.urlopen(req)
    # jsondata = res.read()

    background_image = "https://images.mafengwo.net/images/signup/wallpaper/26.jpg"

    if request.method == "POST":
        user_name = request.form["username"]
        password = request.form["password"]

        remember = request.form.get('rememberme')

        user = User.query.filter_by(user_name=user_name).first()

        if user and user.check_password(password):
            session['user_passwd'] = password
            login_user(user,remember=remember)
            return redirect(url_for('itemList'))
        else:
            flash("用户不存在或密码错误",'warning')
    return render_template('login.html', background_image=background_image)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))