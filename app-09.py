from flask import Flask, render_template

app = Flask(__name__)

app.config.from_object('config')

# url 链接
@app.route('/')
def index():
    return render_template('index5.html')

@app.route('/login1/')
def login1():
    return render_template('login1.html')


if __name__ == '__main__':
    app.run()