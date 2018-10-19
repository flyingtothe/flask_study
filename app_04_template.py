from flask import Flask, render_template

app = Flask(__name__)

app.config.from_object('config')

# 模板：模板文件夹必须与应用同一级
@app.route('/')
def index():
    class Person(object):
        name = 'liu'
        age = 18

    p = Person()

    # 参数：第一个参数指定模板，其他参数指向改模板中的变量，，参数名与变量名必须一致
    # 直接传参
    # return render_template('index.html', username='lll')
    # 以字典形式传参
    context = {
        'username' : 'lll',
        'age' : 15,
        'gender' : 'cai',
        'person' : p,
        'websites' : {
            'baidu' : 'www.baidu.com',
            'google' : 'www.google.com'
        }
    }
    # return render_template('index.html', context=context) # 模板中变量调用 {{变量.属性}}

    # 模板渲染
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run()