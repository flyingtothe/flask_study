from flask import Flask, render_template, request, g
from app_16_utils import login_log

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'index'

@app.route('/login3/', methods=['GET', 'POST'])
def login3():
    if request.method == 'GET':
        return render_template('login3.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')

        # 模拟登陆
        if username == 'liu' and password == '11':
            # 全局变量使用
            g.username = request.form.get('username')
            print(id(g.username))
            g.id = 'ooo'
            login_log()
            return '成功'
        else:
            return '错误'

if __name__ == '__main__':
    app.run()