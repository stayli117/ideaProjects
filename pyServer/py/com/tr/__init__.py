# -*- coding: UTF-8 -*
# 下载所有的车次数据  保存为 train_list.txt文件
import re

import requests


def getTrain_list():
    requests.adapters.DEFAULT_RETRIES = 5
    requests.packages.urllib3.disable_warnings()
    response = requests.get("https://kyfw.12306.cn/otn/resources/js/query/train_list.js?scriptVersion=1.0", stream=True,
                            verify=False)
    status = response.status_code
    if status == 200:
        with open('train_list.txt', 'wb') as of:
            for chunk in response.iter_content(chunk_size=102400):
                if chunk:
                    of.write(chunk)
                    # print(chunk)


# 分析train_list.txt文件 得出火车 出发站到终点站的数据
def trainListStartToEnd():
    global station_start_end_set
    with open('train_list.txt', 'rb') as of:
        text = of.readline()
        tt = text.decode("utf-8")
        ss = tt.replace("},{", "}\n{").replace("2018-", "\n").replace("[", "\n").split("\n")
        m_list = list()
        for s in ss:
            pattern = re.compile(r'(\(\S+-\S+\))')
            match = pattern.search(s)
            if match:
                city =match.group(1)
                m_list.append(city)
        station_start_end_set = set(m_list)
        print(station_start_end_set)






if __name__ == "__main__":
    getTrain_list()
    trainListStartToEnd()

def test():
    a = {"station_train_code":"Z9877(西宁-德令哈)","train_no":"88000Z987703"};
    b = re.compile(r'(\(\S+-\S+\))')
    c = b.search(a)
    print(c)


