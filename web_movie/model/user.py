from web_movie.model.base import Base
from sqlalchemy import  Column,String,Integer
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, autoincrement= True,primary_key=True)
    username = Column(String)
    password = Column(String)

