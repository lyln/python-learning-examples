# -*-coding: utf-8 -*-
#@Author: 'ljd'
#@Time：2016/10/26 17:01
import time
import socket,struct,json
import urllib2

from models import movieItems

# 时间转换类
# time.mktime(tupletime)
# 接受时间元组并返回时间辍（1970纪元后经过的浮点秒数）。
# time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
# 根据fmt的格式把一个时间字符串解析为时间元组
def str2stamp(str):
    tup = time.strptime(str,'%Y-%m-%d %H:%M:%S')
    return time.mktime(tup)

def dt2stamp(dt):
    return time.mktime(dt.timetuple())

def long2ip(ip):
    return socket.inet_ntoa(struct.pack('!L', ip))


def youdao(word):
    qword = urllib2.quote(word)
    baseurl =r'http://fanyi.youdao.com/openapi.do?keyfrom=lyln-fangyi&key=1994600834&type=data&doctype=json&version=1.1&q='
    url = baseurl+qword
    resp = urllib2.urlopen(url)
    fanyi = json.loads(resp.read())
    if fanyi['errorCode'] == 0:
        if 'basic' in fanyi.keys():
            trans = u'%s:\n%s\n%s\n网络释义：\n%s'%(fanyi['query'],''.join(fanyi['translation']),' '.join(fanyi['basic']['explains']),''.join(fanyi['web'][0]['value']))
            return trans
        else:
            trans =u'%s:\n基本翻译:%s\n'%(fanyi['query'],''.join(fanyi['translation']))
            return trans
    elif fanyi['errorCode'] == 20:
        return u'对不起，要翻译的文本过长'
    elif fanyi['errorCode'] == 30:
        return u'对不起，无法进行有效的翻译'
    elif fanyi['errorCode'] == 40:
        return u'对不起，不支持的语言类型'
    else:
        return u'对不起，您输入的单词%s无法翻译,请检查拼写'% word


def getBaiduYunUrl(word):
    m_items = movieItems.query.filter_by(m_title=word).first()
    return m_items
