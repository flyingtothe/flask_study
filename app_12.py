from flask import Flask
from exts import db
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run()