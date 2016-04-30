#!/usr/bin/env python
#coding:utf-8
from flask import Flask
from flask import jsonify
from flask import request
import config
import weixin
app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        tos = request.form.get('phone')
        content = request.form.get('content')
        if tos == '18053514131':
            tos = 'oaqexw-otoH-qb2AlbdbhFVi2kIE'
        weixin.login(username,password)
        weixin.singlesend(tos,content)
        return jsonify({'resp':status})
    elif request.method == 'GET':
        return jsonify({'resp':errstatus})
    else:
        return jdonigy({'resp':'unknown method'})


if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0',debug=True)
