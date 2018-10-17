from flask import Flask, render_template

app = Flask(__name__)

app.config.from_object('config')

'''
filter 过滤器
过滤器可以处理变量，将原始变量经过处理后再展示，作用对象是变量
default 过滤器：当前变量不存在，显示的默认值
length 过滤器：求列表、字符串、字典、元组的长度
'''
@app.route('/')
def index():
    comments = [
        {
            'user': 'liu',
            'content': 'xxx'
        },
        {
            'user': 'lll',
            'content': 'xxxxx'
        }
    ]
    return render_template('index3.html', comments=comments)


if __name__ == '__main__':
    app.run()