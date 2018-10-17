from flask import Flask, render_template

app = Flask(__name__)

app.config.from_object('config')

# 继承和 block
@app.route('/')
def index():
    return render_template('index4.html')

@app.route('/login/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()