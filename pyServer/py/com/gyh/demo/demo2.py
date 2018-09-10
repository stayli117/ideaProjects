#!/usr/bin/env python
# -*- coding: UTF-8 -*

#python 2.7.10
# 动态JS数据爬虫头条

import sys
reload(sys)
sys.setdefaultencoding('utf8')
print sys.getdefaultencoding()

import requests
#引入相关模块
from bs4 import BeautifulSoup
#处理字典乱码
import json
url='http://www.toutiao.com/api/pc/focus/'
data=requests.get(url)
webData=data.text
jsondata=json.loads(webData)
# 处理字典乱码问题
jresult=json.dumps(jsondata, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
print(jresult)
news=jsondata['data']['pc_feed_focus']
# print news
for n in news:
    title = n['title']

    img_url = n['image_url']

    if('media_url' in n):
        url = n['media_url']

    else:
        url=''

    print '---------------'
    print title
    print img_url
    print url
    print(url,title,img_url,u'中文')
    print '中文'