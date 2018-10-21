from flask import Flask
from app_13_exts import db
# 导入模型
from app_13_models import Article

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

# 访问服务器中的 app 需先将 app 插入栈中
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run()