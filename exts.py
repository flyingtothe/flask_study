from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from app_12 import app

app.config.from_object('config')
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], max_overflow=5)
db = declarative_base()