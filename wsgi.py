#!/usr/bin/env python
#coding:utf-8
from flask import Flask
from flask import jsonify
from flask import request
import config
import weixin
app = Flask(__name__)
username = config.username
password = config.password
status = [
    {
        'status': 200,
        'info': '发送成功'
    }
]
errstatus = [
    {   
        'status': 201,
        'info': '不支持GET方式'
    }
]
def phone_to_weixinid(phone):
    if phone in config.phonetoweixinid.keys():
       return config.phonetoweixinid[phone] 
    else:
        return 'phone is not set in config'
       

@app.route('/', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        tos = request.form.get('phone')
        content = request.form.get('content')
        tos = phone_to_weixinid(tos)
        weixin.login(username,password)
        weixin.singlesend(tos,content)
        return jsonify({'resp':status})
    elif request.method == 'GET':
        return jsonify({'resp':errstatus})
    else:
        return jdonigy({'resp':'unknown method'})


if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0',debug=True)
