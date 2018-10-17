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
# Base.metadata.create_all(engine)


# 数据库操作视图
@app.route('/')
def index():
    # 创建 session
    Session = sessionmaker(bind=engine)
    session = Session()

    # 增加
    article1 = Article(title='aa', content='bb')
    # 生成事务，未提交至数据库
    session.add(article1)
    # add_all 列表形式
    session.add_all([
        Article(name='cc', extra='cow'),
        Article(name='dd', extra='cowcow')
    ])
    # 事务
    session.commit()

    # 查询
    # result = session.query(Article).filter_by(title='aa').first()
    # print('title:%s' % result.title)
    # print('content:%s' % result.content)

    # 修改
    # article = session.query(Article).filter_by(title='aa').first()
    # article.title = 'new title'
    # session.commit()

    # 删除
    # session.query(Article).filter_by(content='bb').delete()
    # session.commit()

    # return 'hello world'


if __name__ == '__main__':
    app.run()