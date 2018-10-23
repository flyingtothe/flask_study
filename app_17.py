from flask import Flask, render_template, request, session, url_for, redirect, g
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def hello_world():
    return render_template('index7.html')

@app.route('/login4/', methods=['GET', 'POST'])
def login4():
    if request.method == 'GET':
        return render_template('login4.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'liu' and password == '11':
            session['username'] = request.form.get('username')
            return '成功'
        else:
            return '失败'

@app.route('/edit/')
def edit():
    # if hasattr(g, 'username'):
    #     return render_template('edit.html')
    # else:
    #     return redirect(url_for('login4'))

    return render_template('edit.html')

# 钩子函数（hookfunction）
# brfore_request:在请求之前执行（在试图函数前）
# 只是一个装饰器，可将需要设为钩子函数的代码放到视图函数执行之前
@app.before_request
def mybefore():
    if session.get('username'):
        g.username = session.get('username')


@app.context_processor
def mycontext():
    # username = session.get('username')
    # if username:
    #     return {'username': username}
    return {'username':'liu'}


if __name__ == '__main__':
    app.run()