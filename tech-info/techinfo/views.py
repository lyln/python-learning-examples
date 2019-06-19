# -*-coding: utf-8 -*-
#@Author: 'walkerlee'
#@Time: 2019/1/10 下午5:03

from flask import render_template,request
from techinfo import app
from utils import httpUtil,html2json
@app.route('/')
def index():
    url = 'https://extension-ms.juejin.im/resources/cnblogs'
    offset = request.args.get('offset')
    res =httpUtil.httpUtilPost(url,offset)

    return  render_template('index.html',article_lists=res['data'])

@app.route('/article')
def article_detial():
    url = request.args.get('url')
    print url
    article = html2json.cnblog(url)
    return  render_template('article.html',article=article)
