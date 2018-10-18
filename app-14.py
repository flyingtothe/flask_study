from flask import Flask
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

app = Flask(__name__)
app.config.from_object('config')
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], max_overflow=5)
Base = declarative_base()


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run()