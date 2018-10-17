from flask import Flask, render_template

app = Flask(__name__)

app.config.from_object('config')

# if 判断
@app.route('/<is_login>/')
def index(is_login):
    if is_login == '1':
        user = {
            'username' : 'ljk',
            'age' : 11
        }
        return render_template('index1.html', user=user)
    else:
        return render_template("index1.html")


if __name__ == '__main__':
    app.run()