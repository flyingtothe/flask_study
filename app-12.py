from flask import Flask
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

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
    author_id = Column(Integer, ForeignKey('users.id')) # 外键

    # 给模型添加 author 属性，访问该属性的数据，与访问普通模型一样
    # backref 定影反向引用，通过 user.articles 访问模型的所有内容
    author = relationship('Users', backref=backref('articles'))

# Base.metadata.create_all(engine)


@app.route('/')
def index():
    Session = sessionmaker(bind=engine)
    session = Session()

    # 添加用户
    # user1 = Users(username='liu')
    # session.add(user1)
    # session.commit()

    # 添加文章
    # article = Article(title='aa', content='bb', author_id=1)
    # session.add(article)
    # session.commit()

    # 查找文章标题为 aa 的作者
    '''
    filter用类名.属性名，比较用==，filter_by直接用属性名，比较用=
    个人觉得最重要的区别是filter不支持组合查询，只能连续调用filter来变相实现
    而filter_by的参数是**kwargs，直接支持组合查询
    '''
    # article = session.query(Article).filter_by(title='aa').first()
    # author_id = article.author_id
    # user = session.query(Users).filter_by(id = author_id).first()
    # print(user.username)

    # 反向访问（通过模型，访问数据库）
    # article = Article(title='aaa', content='bbb')
    # article.author = session.query(Users).filter(Users.id == 1).first()
    # session.add(article)
    # session.commit()

    # article = session.query(Article).filter_by(title='aaa').first()
    # print('username:%s ' % article.author.username)

    user = session.query(Users).filter(Users.username == 'liu').first()
    result = user.articles
    for article in result:
        print('*' * 10)
        print(article.title)

    return 'hello world'


if __name__ == '__main__':
    app.run()