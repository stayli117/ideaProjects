#!/usr/bin/env python
# -*- coding: UTF-8 -*

#获取城市PM2.5浓度
# 爬取PM信息
#python 2.7.10

import urllib2
import threading
from time import ctime
from bs4 import BeautifulSoup

#解决 python在安装时，默认的编码是ascii，
# 当程序中出现非ascii编码时，
# python的处理常常会报这样的错UnicodeDecodeError: 'ascii' codec can't decode byte 0x?? in position 1: ordinal not in range(128)，
# python没办法处理非ascii编码的，
# 此时需要自己设置将python的默认编码，一般设置为utf8的编码格式。
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def getPM25(cityName):
    site='http://www.pm25.com/'+cityName+'.html'
    html=urllib2.urlopen(site)
    soup=BeautifulSoup(html,'html.parser')

    city=soup.find(class_='bi_loaction_city') #城市名称
    aqi=soup.find("a",{"class","bi_aqiarea_num"}) #AQI指数
    quality=soup.select(".bi_aqiarea_right span")#空气质量

    result=soup.find("div",class_='bi_aqiarea_bottom')
    fresult=soup.find("p",class_='bi_info_tips')
    wresult=soup.find("p",class_='bi_info_weather')

    print city.text+u'AQI指数'+aqi.text+u'\n空气质量：'+result.text
    print '空气质量'+quality[0].text +'\n:'+quality[1].text
    print '测试:--> '+fresult.text
    print wresult.text
    print wresult.img['src']
    print '*'*20+ctime()+'*'*20

def one_thread():
    print 'One_thread Start: '+ctime()+'\n'
    getPM25('beijing')
    # getPM25('zhengzhou')

def two_thread():
    print('Two_thread Start: ' +ctime()+"\n")
    thrads=[]
    t1=threading.Thread(target=getPM25('beijing',))
    thrads.append(t1)
    t2=threading.Thread(target=getPM25('zhengzhou',))
    thrads.append(t2)
    for t in  thrads:
        t.start()

if __name__=='__main__':
    one_thread()
    # print '\n'*2
    # two_thread()