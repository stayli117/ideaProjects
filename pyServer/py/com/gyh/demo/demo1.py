#!/usr/bin/env python
# -*- coding: UTF-8 -*

#python 2.7.10
# 简单Http

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import requests
#引入相关模块
from bs4 import BeautifulSoup
#处理字典乱码
import json
url='http://news.qq.com/'
data=requests.get(url)
# print data.status_code
# print data.content

webData=data.text
# 解析文本
soup=BeautifulSoup(webData,'lxml')
# 从解析文件中通过select选择器定位指定的元素，返回一个列表
news_titles =soup.select("div.text > em.f14 > a.linkto")

# 对返回的列表进行遍历

for n in news_titles:
    #提取标题和链接信息
    title = n.get_text()
    link = n.get('href')
    jsonlist ={
        '标题':title,
        '链接':link
    }
    # 处理字典乱码问题
    jresult=json.dumps(jsonlist, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
    print(jresult)

# cookie 模拟登陆

cookie = {
    "cisession":"19dfd70a27ec0eecf1fe3fc2e48b7f91c7c83c60",
    "CNZZDATA100020196":"1815846425-1478580135-https%253A%252F%252Fwww.baidu.com%252F%7C1483922031",
    "Hm_lvt_f805f7762a9a237a0deac37015e9f6d9":"1482722012,1483926313",
    "Hm_lpvt_f805f7762a9a237a0deac37015e9f6d9":"1483926368"
}

url = 'https://www.jianshu.com/u/7b77de9ad37b'
wbdata = requests.get(url,cookies=cookie).text
soup = BeautifulSoup(wbdata,'lxml')
print(soup)
