from flask import Flask, url_for

app = Flask(__name__)

# 导入配置文件
app.config.from_object('config')

# url 与 视图函数 hello_world 的映射
@app.route('/')
def index():
    print(url_for('my_list'))
    print(url_for('article', id='ahs'))
    return 'Hello World!'

# 根据视图函数获取 url(反转)
@app.route('/list/')
def my_list(id):
    return 'list'

# 带参映射
@app.route('/article/<id>/')
def article(id):
    return '请求的参数：%s' % id


if __name__ == '__main__':
    app.run()
