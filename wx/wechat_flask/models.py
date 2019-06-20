from db import db
from flask_login import UserMixin

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


class movieItems(db.Model):
    __tablename__ = "m_items"
    m_id = db.Column(db.BigInteger,primary_key=True)
    m_title = db.Column(db.String(255))
    m_url = db.Column(db.String(255))
    m_type = db.Column(db.INTEGER)
    m_image = db.Column(db.String(255))
    m_desc = db.Column(db.String(255))
    def __init__(self,m_id,m_title,m_url,m_type,m_image,m_desc):
        self.m_id = m_id
        self.m_title = m_title
        self.m_url = m_url
        self.m_type = m_type
        self.m_image = m_image
        self.m_desc = m_desc


    def __repr__(self):
        return '<m_items %r>' %self.__tablename__


class User(db.Model, UserMixin):
    __tablename__ = 'm_user'
    user_id = db.Column(db.BIGINT, primary_key=True)
    user_name = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, user_id=None, user_name=None, password=None):
        self.user_id = user_id
        self.user_name = user_name
        self.password = self.set_password(password)

    def set_password(self, password):
        return generate_password_hash(password, method="pbkdf2:sha1:100", salt_length=2)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.user_id