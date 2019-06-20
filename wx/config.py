# -*-coding: utf-8 -*-
#@Author: 'ljd'
#@Time：2016/12/12 21:54
CSRF_ENABLED = True
SECRET_KEY = 'lyln_movie'

MYSQL_HOST='127.0.0.1'
DB_USER = 'root'
DB_PASSWD = 'root@9527'
DB_NAME = 'lyln'

DB_URL = 'mysql://' + DB_USER + ':' + DB_PASSWD +'@' + MYSQL_HOST + '/' + DB_NAME

# page_size
PER_PAGE = 5
