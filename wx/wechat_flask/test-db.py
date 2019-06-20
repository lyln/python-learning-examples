# -*- coding: utf-8 -*-
# @Time    : 2017/10/24 下午6:02
# @Author  : lyln


#添加密码
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

password_hash = generate_password_hash('root@9527',method="pbkdf2:sha1:100",salt_length=2)

print password_hash

print check_password_hash(password_hash, 'root@9527')