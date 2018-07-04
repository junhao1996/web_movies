from sqlalchemy.orm import sessionmaker

from web_movie.model import Img, User, Movie
from web_movie.model.base import engine


class DB():
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create(self, imgname):
        img = Img(imgname=imgname)
        self.session.add(img)
        self.session.commit()

    def read_img(self):
        s = self.session.query(Img).all()
        return s

    def readmovie(self,id):
        res = self.session.query(Movie).filter(Movie.id ==id).first()
        return res

    def create_movie(self,title,content):
        movie = Movie(title = title,content = content)
        self.session.add(movie)
        self.session.commit()

    def create_user(self, username, password):
        user = User(username=username, password=password)
        self.session.add(user)
        self.session.commit()


#
if __name__ =="__main__":
    d = DB()
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
