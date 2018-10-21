from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# 使用 flask—script，需要使用 manage.py 文件
@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run()