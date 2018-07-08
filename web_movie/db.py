from sqlalchemy.orm import sessionmaker

from web_movie.model import Img, User, Movie
from web_movie.model.base import engine
from sqlalchemy import func


class DB():
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create(self, imgname):
        img = Img(imgname=imgname)
        self.session.add(img)
        self.session.commit()

    def read_img(self,pageset):
        s = self.session.query(Img).slice((pageset-1)*10,pageset*10).all()
        return s
    def read_count(self):
        s = self.session.query(func.count(Img.id)).first()
        self.session.commit()
        return s

    def readmovie(self, id):
        res = self.session.query(Movie).filter(Movie.id == id).first()
        return res

    def create_movie(self, title, content,actor,movie_type,time,logintime):
        movie = Movie(title=title, content=content,actor = actor,movie_type = movie_type,time = time,logintime = logintime)

        self.session.add(movie)
        self.session.commit()

    def get_movietype(self):
        res = self.session.query(Movie.movie_type).all()
        return set(res)
    def get_movie(self,type):
        res = self.session.query(Movie).filter(Movie.movie_type==type).all()
        return res

    def create_user(self, username, password):
        user = User(username=username, password=password)
        self.session.add(user)
        self.session.commit()


if __name__ == "__main__":
    d = DB()
    # a = d.get_movietype()
    # print(a)
    # d.create_movie("111","aaa","zhangsan","科技","1995","106")
    # count = d.read_count()
    # allpage = int(count[0]/5)
    # print(type(count))
    # print(count[0])
    # print(allpage)
    a = d.read_img(1)
    # print(a)
    # for i,j in enumerate(a):
    #     print(i,j)








    # for i in range(10):
    #     d.create_movie("三国演绎","sdfsfgsgdsfgdsfgjndsgiudsbpfgin safjlskdjfnsdiozgisi")
#     list1 = [
#
#         "KJ71H3Tchw.jpg",
#         "cTnkWv7ZqX.jpg",
#         "ugtplEslO5.jpg",
#         "gHJDCVA1fp.jpg",
#         "bHI78E7BrB.jpg"]
#     for i in list1:
#         d.create(i)
