# -*-coding: utf-8 -*-
#@Author: 'walkerlee'
#@Time: 2019/1/11 上午10:24

from bs4 import BeautifulSoup
import json
from techinfo.utils import httpUtil


def cnblog(url):

    ## 获取网页主体
    html = httpUtil.httpUtilGet(url)

    soup = BeautifulSoup(html, 'html5lib')
    title = soup.find_all('title')[0].get_text()
    # article = str(soup.find_all('article')[0])
    contents_str = soup.find_all(id='cnblogs_post_body')[0]
    # print type(contents_str.encode("utf-8"))
    # contents = json.dumps(contents_str).decode("unicode-escape")
    contents = contents_str.encode("utf-8")
    # print contents[0]

    article = {'title':title,'contents':contents}
    return article