#!/usr/bin/env python
#coding:utf-8
from flask import Flask
from flask import jsonify
from flask import request
import weixin
app = Flask(__name__)

'''@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'
    '''
status = [
    {
        'status': 200,
        'info': '发送成功'
    }
]

@app.route('/', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        tos = request.form.get('phone')
        content = request.form.get('content')
        if tos == '18053514131':
            tos = 'oaqexw-otoH-qb2AlbdbhFVi2kIE'
        weixin.login('duhe4841384@163.com','Xlb890213')
        weixin.singlesend(tos,content)
        return jsonify({'resp':status})
    elif request.method == 'GET':
        data = request.args
        print data
        weixin.login('duhe4841384@163.com','Xlb890213')
        weixin.singlesend(data['tos'],data['content'])
        #weixin.singlesend('oaqexw-otoH-qb2AlbdbhFVi2kIE',msg)
        #send_mail(data['tos'],data['content'])
        return jsonify({'resp':status})
    else:
        return 'no data'


if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0',debug=True)
