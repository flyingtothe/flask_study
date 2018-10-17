from flask import Flask
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

app.config.from_object('config')

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], max_overflow=5)

Base = declarative_base()
# 用户表
class Users(Base):
    __tablename__ = 'users'
    # 类型需要导入
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)

class Article(Base):
    __tablename__ = 'article'
    # 类型需要导入
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    # 外键
    author_id = Column(Integer, ForeignKey('users.id'))

Base.metadata.create_all(engine)


@app.route('/')
def index():
    Session = sessionmaker(bind=engine)
    session = Session()

    # 添加用户
    user1 = Users(username='liu')
    session.add(user1)
    session.commit()
    return 'hello world'


if __name__ == '__main__':
    app.run()