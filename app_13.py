from flask import Flask
from app_13_exts import db
# 导入模型
from app_13_models import Article

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

# 使用上下文将 app 加载至栈中
# with app.app_context():
#     db.create_all()

# flask-migrate 需要与 flask-script 配合使用


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run()