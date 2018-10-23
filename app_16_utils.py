from flask import g
# 工具类
def login_log():
    print('用户名：%s' % g.username)

def login_ip_log(ip):
    pass