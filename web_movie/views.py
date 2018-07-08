from flask import Blueprint, render_template, abort, request

from web_movie.db import DB

new_blueprint = Blueprint("web_movie", __name__, template_folder='templates')

# 这是 app设置的方式：app = Flask(__name__, static_folder='', template_folder='')
# 这行设置这个项目的静态根目录和模版目录，直接暴露assets文件夹为静态
db = DB()


@new_blueprint.route("/show/<int:newpage>", methods=['GET', "POST"])
def show(newpage):
    res = db.read_img(newpage)
    for i in res:
        print(i.imgname)

    count = db.read_count()[0]
    allpage = int(count / 8)+1
    dict1 = {
        "allpage": allpage,
        # 总页数
        "count": count,
        # 总条目
        "newpage": newpage
        # 当前页
    }
    return render_template("show.html", dict1=dict1, result=res)


# def get_page(total,p):
#     show_page = 5   # 显示的页码数
#     pageoffset = 2  # 偏移量
#     start = 1    #分页条开始
#     end = total  #分页条结束
#
#     if total > show_page:
#         if p > pageoffset:
#             start = p - pageoffset
#             if total > p + pageoffset:
#                 end = p + pageoffset
#             else:
#                 end = total
#         else:
#             start = 1
#             if total > show_page:
#                 end = show_page
#             else:
#                 end = total
#         if p + pageoffset > total:
#             start = start - (p + pageoffset - end)
#     #用于模版中循环
#     dic = range(start, end + 1)
#     return dic


@new_blueprint.route("/show_content/<id>", methods=['GET', "POST"])
def show_content(id):
    print(id, 44444444444)
    res = db.readmovie(id)
    # print(res)
    return render_template("show_content.html", res=res)


@new_blueprint.route("/movie_type", methods=["GET", "POST"])
def movietype():
    res = db.get_movietype()
    return render_template("movietype.html", result=res)


@new_blueprint.route("/show_movie/<string:tt>", methods=["GET", "POST"])
def show_movie(tt):
    res = db.get_movie(tt)
    print("qqqq")
    return render_template("show_typemovie.html", result=res)


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
