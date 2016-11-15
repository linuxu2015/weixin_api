### [2016.11.15]微信登录添加验证码登录了，微信公众号无法使用了……
# 基于minos的微信发送报警信息api
minos中报警的发送方式为短息和邮件，这个api就是将短信替换为通过微信的公众号发送。
## 安装方法
我们使用virtualenv来管理Python环境，yum安装需切到root账号
```bash
yum install -y python-virtualenv

$ cd /path/to/weixin_api/
$ virtualenv ./env

$ ./env/bin/pip install -r pip_requirements.txt
```
## 配置方法
```bash
vim config.py
username = ''  #微信公众号帐号
password = ''  #微信公众号密码


phonetoweixinid = {
'phone':'id'  #手机号：微信id，因为minos手机号是验证的，不是手机号格式无法填写，所以加了这个转换。
这个微信id是关注公众号之后在公众号后台生成的，可以去公众号后台，点击关注的用户，在url里有一串就是该id
类似这样的：oaqexw-otoH-qb2AlbdbhFVi2kIE
}
```
请求示例
```bash
curl 192.168.101.189:5000 -d 'phone=oaqexw-otoH-qb2AlbdbhFVi2kIE&content=message'
```
minos配置
```python
"sms": {
        "addr": "http://ip:port",
        "method": "POST",
        "params": {
            "phone": "{phone}",
            "content": "{content}"
        }
    }
```
## 进程管理
统一使用的minos的管理工具control
```bash
./control start 启动进程
./control stop 停止进程
./control restart 重启进程
./control status 查看进程状态
./control tail 用tail -f的方式查看var/app.log
```
