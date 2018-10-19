from flask import Flask
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

app = Flask(__name__)
app.config.from_object('config')
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], max_overflow=5)
Base = declarative_base()

article_tag = Table(
    'article_tag',
    # 组合主键
    Base.metadata,
    Column('article_id', Integer, ForeignKey('article.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True)
)

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)

    tags = relationship('Tag', secondary=article_tag, backref=backref('articles'))   # 关联关系设置

class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

Base.metadata.create_all(engine)

@app.route('/')
def index():

    Session = sessionmaker(bind=engine)
    session  =Session()

    # article1 = Article(title='aaa')
    # article2 = Article(title='bbb')

    # tag1 = Tag(name='111')
    # tag2 = Tag(name='222')

    # # 多对多关系建立
    # article1.tags.append(tag1)
    # article1.tags.append(tag2)
    # article2.tags.append(tag1)
    # article2.tags.append(tag2)

    # session.add(article1)
    # session.add(article2)
    # session.add(tag1)
    # session.add(tag2)

    # session.commit()

    article1 = session.query(Article).filter_by(title='aaa').first()
    tags = article1.tags
    for tag in tags:
        print(tag.name)

    return 'hello world'


if __name__ == '__main__':
    app.run()