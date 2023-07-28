import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from database import Base

class User(Base):
    __tablename__ = "users"

    uid = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_time = Column(DateTime, default=datetime.datetime.utcnow)
    
class Post(Base):
    __tablename__ = "posts"

    pid = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False)
    created_time = Column(DateTime, default=datetime.datetime.utcnow)
    uid  = Column(Integer, ForeignKey('users.uid'))
    



