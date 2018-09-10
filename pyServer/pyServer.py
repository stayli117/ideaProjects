# -*- coding: UTF-8 -*
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'




@app.route('/test/chinese/encoding')
def chinese_encoding():
    global name, type
    if True:
        name='中文格式'
        return name
    else:
        type='编码utf-8'
    return '测试中文编码'+type









if __name__ == '__main__':
    app.run(port=8888)
