from sqlalchemy import Column, Integer, String
from exts import db

class Article(db):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)