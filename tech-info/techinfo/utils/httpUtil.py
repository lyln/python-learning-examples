# -*-coding: utf-8 -*-
#@Author: 'walkerlee'
#@Time: 2019/1/10 下午7:48

import random
import requests
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

useragents = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    ]

def httpUtilPost(url,offset=0):
    headers = {
        'User-Agent': random.choice(useragents)
    }

    body = {
        'limit': 20,
        'offset': offset
    }

    # parames = json.dumps(body)

    #post获取网页
    print url
    r = requests.post(url,headers=headers,data=body)
    return r.json()

# url = 'https://extension-ms.juejin.im/resources/cnblogs'
# res = httpUtil(url)

# print res['data']
def httpUtilGet(url):
    headers = {
        'User-Agent': random.choice(useragents)
    }
    #post获取网页
    r = requests.get(url,headers=headers)
    return r.text