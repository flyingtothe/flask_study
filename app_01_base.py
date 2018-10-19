'''
文档：
http://docs.jinkan.org/docs/flask/index.html
http://flask.pocoo.org/
'''
from flask import Flask

# 初始化一个 Flask 对象
# 需要传递参数 __name__
# 1.方便 flask 框架寻找资源
# 2.方便 flask 插件出现错误时，寻找错误位置
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # 启动应用服务器，来接收用户请求
    # while true:
    #   listen()
    app.run(debug=True)     # 设置为调试模式
