from flask import Blueprint, render_template, abort

from web_movie.db import DB

new_blueprint = Blueprint("web_movie", __name__, template_folder='templates')

# 这是 app设置的方式：app = Flask(__name__, static_folder='', template_folder='')
# 这行设置这个项目的静态根目录和模版目录，直接暴露assets文件夹为静态
db = DB()


@new_blueprint.route("/show", methods=['GET', "POST"])
def show():
    res = db.read_img()
    for i in res:
        print(i.imgname)
    return render_template("show.html", result=res)
@new_blueprint.route("/show_content/<id>", methods=['GET', "POST"])
def show_content(id):
    print(id,44444444444)
    res = db.readmovie(id)
    # print(res)
    return render_template("show_content.html",res = res)


@new_blueprint.route("/add", methods=['GET', "POST"])
def add():

    list1 = [
        "TKZfKLDuEM.jpg",
        "KJ71H3Tchw.jpg",
        "cTnkWv7ZqX.jpg",
        "ugtplEslO5.jpg",
        "gHJDCVA1fp.jpg",
        "bHI78E7BrB.jpg"]
    # for i in list1:
    #     db.create(i)
    # return render_template("show.html")

