from sqlalchemy import Column, Integer, String

from web_movie.model.base import Base


class Img(Base):
    __tablename__ = 'img'
    id = Column(Integer, autoincrement= True,primary_key=True)
    imgname = Column(String)