from flask import Flask, redirect, url_for

app = Flask(__name__)

app.config.from_object('config')

# 重定向
@app.route('/')
def index():
    # 重定向目标
    login_url = url_for('login')
    # 重定向到登录页
    return redirect(login_url)
    return '首页'

@app.route('/login/')
def login():
    return '登陆页'

# 模拟登陆判断
@app.route('/question/<is_login>/')
def question(is_login):
    if is_login == '1':
        return '问答页面'
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()