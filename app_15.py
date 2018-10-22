from flask import Flask, render_template, request

app = Flask(__name__)

# get
@app.route('/')
def index():
    return render_template('index6.html')

@app.route('/search/')
def search():
    return '参数：%s' % request.args.get('q')

# post
# 默认视图函数，只能用 get 请求。使用 post 需声明
@app.route('/login2/', methods=['GET', 'POST'])
def login2():
    if request.method == 'GET':
        return render_template('login2.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)