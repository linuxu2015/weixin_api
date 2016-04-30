# 基于minos的微信发送报警信息api
minos中报警的发送方式为短息和邮件，这个api就是将短信替换为通过微信的公众号发送。
## 配置方法
vim config.py
username = ''  #微信公众号帐号
password = ''  #微信公众号密码

phonetoweixinid = {
'phone':'id'  #手机号：微信id，这个微信id是关注公众号之后在公众号后台生成的，可以去公众号后台，点击关注的用户，在url里有一串就是该id
类似这样的：oaqexw-otoH-qb2AlbdbhFVi2kIE
}
请求示例
curl 192.168.101.189:5000 -d 'phone=oaqexw-otoH-qb2AlbdbhFVi2kIE&content=message'
minos配置
"sms": {
        "addr": "http://ip:port",
        "method": "POST",
        "params": {
            "phone": "{phone}",
            "content": "{content}"
        }
    }
