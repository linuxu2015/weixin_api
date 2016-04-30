#!/usr/bin/env python
# coding:utf-8
"""
微信公众平台管理界面
"""
import requests
import hashlib
import random
import json
import sys

session=requests.session()
session.headers={
                'User-Agent':'Mozilla/5.0 (<a href="http://www.ttlsa.com/windows/" title="windows"target="_blank">Windows</a> NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
                'Accept-Encoding': 'deflate',
                'DNT': '1',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With': 'XMLHttpRequest',
                'Referer': 'https://mp.weixin.qq.com/',
                'Connection': 'keep-alive',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache'
                }
token=None
def login(username,pwd):
    """登录"""
    #正确响应：{"base_resp":{"ret":0,"err_msg":"ok"},"redirect_url":"\/cgi-bin\/home?t=home\/index&lang=zh_CN&token=898262162"}
    global token
    pwd=hashlib.md5(pwd).hexdigest()
    url='https://mp.weixin.qq.com/cgi-bin/login?lang=zh_CN'
    data={'f':'json',
          'imgcode':'',
          'pwd':pwd,
          'username':username}
    res=session.post(url,data)
  #  print 'response: login',res.text
    j=json.loads(res.text)
    status=j['base_resp']['err_msg']
    if status=='ok':
        token=j['redirect_url'].split('=')[-1]
        return True
    return False

def singlesend(tofakeid,content):
    """发送消息给单个人
    多次发送消息可能需要发送心跳信息（未测试）"""
    #正确响应：{"base_resp":{"ret":0,"err_msg":"ok"}}
    url='https://mp.weixin.qq.com/cgi-bin/singlesend'
    data={'ajax':'1',
            'content':content,
            'f':'json',
            'imgcode':'',
            'lang':'zh_CN',
            'random':str(random.random()),
            't':'ajax-response',
            'tofakeid':tofakeid,
            'token':token,
            'type':'1',
            }
    res=session.post(url,data)
 #   print 'response: singlesend',res.text
    j=json.loads(res.text)
    status=j['base_resp']['err_msg']
    if status=='ok':
        return True
    return False

def masssend(content):
    """群发消息"""
    #正确响应：{"ret":"0", "msg":"ok"}
    url='https://mp.weixin.qq.com/cgi-bin/masssend'
    data={'ajax':'1',
            'city':'',
            'content':content,
            'country':'',
            'f':'json',
            'groupid':'-1',
            'imgcode':'',
            'lang':'zh_CN',
            'province':'',
            'random':str(random.random()),
            'sex':'0',
            'synctxnews':'0',
            'synctxweibo':'0',
            't':'ajax-response',
            'token':token,
            'type':'1'
            }
    res=session.post(url,data)
#    print 'response: masssend',res.text
    j=json.loads(res.text)
    if j['msg']=='ok':
        return True
    return False

if __name__=='__main__':
    res=login('','')
    print 'response: login',res
    if not res:
        sys.exit()

    #群发
    #res=masssend('呵呵')
    #print 'response: masssend',str(res)
    
    #发送给单人
    res=singlesend('oaqexw-otoH-qb2AlbdbhFVi2kIE','message')
    print 'response: singlesend',str(res)
