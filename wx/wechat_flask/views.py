#-*- coding:utf-8 -*-
__author__ = 'ljd'

from flask import render_template,request,abort,url_for,redirect,send_file,Blueprint
from wechat_flask import app
from wechatpy import parse_message, create_reply
from wechatpy.utils import check_signature
from wechatpy.exceptions import (
    InvalidSignatureException,
    InvalidAppIdException,
)
from wechatpy.replies import ImageReply
from wechatpy.replies import ArticlesReply
from wechatpy.utils import ObjectDict

from utils import getBaiduYunUrl
from models import movieItems
from db import db
import config
import urllib2,json,math
from flask_login import login_required,current_user


def list(self, page, limit, query):
    total = movieItems.query.count()
    print page
    print limit
    print query
    print total
    m_items = movieItems.query.limit(limit).offset(query).all()
    return m_items, total

@app.route('/')
@login_required
def itemList():
    # m_items = movieItems.query.all()
    # user_name = current_user.user_name
    # return render_template("index.html",m_items=m_items,user_name=user_name)

    page = request.args.get('page','1')  # 获取页码
    if page == 'None':
        page = '1'
    pagination = movieItems.query.paginate(int(page), config.PER_PAGE, error_out=True)
    m_items = pagination.items

    user_name = current_user.user_name

    total=pagination.total #数据总条数
    total=total/config.PER_PAGE   #页数的定义
    total=int(math.ceil(total))#取整进一
    return render_template('index.html',m_items = m_items, pagination = pagination ,total = total,user_name=user_name)


@app.route('/add_rules')
def addRules():
    return render_template('add_rules.html')

@app.route('/modify_rules',methods=["GET"])
def modifyRules():
    m_id = request.args.get("m_id")
    print m_id

    m_item = movieItems.query.filter_by(m_id=m_id).first()
    return render_template('modify_rules.html',m_item=m_item)

@app.route('/save_rules',methods=['POST'])
def saveRules():
    m_id = request.form["inputId"]
    m_title = request.form["inputTitle"]
    m_url = request.form["inputUrl"]
    m_type = request.form["inputType"]
    m_image = request.form["inputImageUrl"]
    m_desc = request.form["inputDesc"]


    m_item = movieItems.query.filter_by(m_id=m_id).first()
    if m_item is not None:
        # update
        m_item.m_id = m_id
        m_item.m_title = m_title
        m_item.m_url = m_url
        m_item.m_type = m_type
        m_item.m_image= m_image
        m_item.m_desc = m_desc
        db.session.add(m_item)
    else:
        # add
        m_item = movieItems(m_id=m_id,m_title=m_title,m_url=m_url,m_type=m_type,m_image=m_image,m_desc=m_desc)

        db.session.add(m_item)

    if db.session.commit() == None:
        return redirect(url_for("itemList"))
    else:
        return '添加失败！'


@app.route('/delete_rules',methods=['POST'])
def deleteRules():
    m_id = request.values.get('m_id')

    m_item = movieItems.query.filter_by(m_id=m_id).first()

    if m_item is not None:
        db.session.delete(m_item)
        db.session.commit()
        return 'ok'
    else:
        return 'error'


TOKEN = 'mywxlyln'
@app.route('/',methods=['GET', 'POST'])
def wxapi():

    if len(request.args) > 3:
        signature = request.args.get('signature', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        print signature + timestamp + nonce
        encrypt_type = request.args.get('encrypt_type', 'raw')
        msg_signature = request.args.get('msg_signature', '')
        try:
            check_signature(TOKEN, signature, timestamp, nonce)
        except InvalidSignatureException:
            abort(403)
    if request.method == 'GET':
        echo_str = request.args.get('echostr', '')
        return echo_str

    # POST request
    if encrypt_type == 'raw':
        # plaintext mode
        msg = parse_message(request.data)
	print msg
	print type(msg.content)
        if msg.type == 'text':
	    if type(msg.content).__name__ == "unicode":
                content = msg.content.encode('UTF-8')
            movieItems = getBaiduYunUrl(content)
            if movieItems is None:
                res = '没有找到您想要的资源，添加微信：irisloveli 反馈'
                reply = create_reply(res, msg)
            elif movieItems.m_type == 6:
                #图文回复
                print msg
                reply = ArticlesReply(message=msg)

                article = ObjectDict()
                article.title = movieItems.m_title
                article.description = movieItems.m_desc
                article.image = movieItems.m_image
                article.url = movieItems.m_url

                reply.add_article(article)


            else:
                #默认0 文本回复
                res = movieItems.m_title + ',' + movieItems.m_url
                reply = create_reply(res, msg)



        else:
            reply = create_reply('Sorry, can not handle this for now', msg)
        return reply.render()
    # else:
    #     # encryption mode
    #     from wechatpy.crypto import WeChatCrypto
    #
    #     crypto = WeChatCrypto(TOKEN, AES_KEY, APPID)
    #     try:
    #         msg = crypto.decrypt_message(
    #             request.data,
    #             msg_signature,
    #             timestamp,
    #             nonce
    #         )
    #     except (InvalidSignatureException, InvalidAppIdException):
    #         abort(403)
    #     else:
    #         msg = parse_message(msg)
    #         if msg.type == 'text':
    #             reply = create_reply(msg.content, msg)
    #         else:
    #             reply = create_reply('Sorry, can not handle this for now', msg)
    #         return crypto.encrypt_message(reply.render(), nonce, timestamp)



@app.route('/ip')
def view_origin():
    """Returns Origin IP."""
    return request.headers.get('X-Forwarded-For', request.remote_addr)

@app.route('/player')
def dplayer():
    return render_template('player.html')

@app.route('/play')
def play():
    play_url = request.form["play"]
    print play_url
    return render_template('player.html',play_url=play_url)