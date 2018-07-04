from sqlalchemy import Column, Integer, String

from web_movie.model.base import Base


class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, autoincrement= True,primary_key=True)
    title = Column(String)
    content = Column(String)
    actor = Column(String)
    movie_type = Column(String)
    time = Column(String)
    logintime = Column(String)
