from flask import Flask
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

app.config.from_object('config')

# 连接数据库
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], max_overflow=5)

# 创建类与表的映射
Base = declarative_base()

# 创建于数据库中表对应的模型类
class Article(Base):
    __tablename__ = 'article'
    # 类型需要导入
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)

# 创建表
Base.metadata.create_all(engine)


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run()