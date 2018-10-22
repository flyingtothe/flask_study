'''
一般情况：将用户信息加密，存放于服务器的session中，并将产生的唯一一个 sessionID 反回给浏览器
flask：将数据加密后，放入 session 中，再将 session 存放到 cookie 中，再次请求时，读取 cookie->session->数据
'''
from flask import Flask, session
import os
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

# 将数据添加至 session，与操作字典相同
@app.route('/')
def hello_world():
    session['username'] = 'aaaa'
    # 未指定 session 过期时间，默认关闭浏览器后失效
    # permanent 默认过期时间为31天
    session.permanent = True
    return 'hello world'

# 读取 session
@app.route('/get/')
def get():
    # session.get['username']       # username 不存在会抛出异常
    # session.get('username')       # 返回 null
    return session.get('username')

# 删除
@app.route('/delete/')
def delete():
    print(session.get('username'))
    session.pop('username')
    print(session.get('username'))
    return 'success'

# 清空 session 中所有数据
@app.route('/clear/')
def clear():
    print(session.get('username'))
    session.clear()
    print(session.get('username'))
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)