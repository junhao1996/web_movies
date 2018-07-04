from flask import Flask, render_template

from web_movie.db import DB
from web_movie.views import new_blueprint

app = Flask('web_movie')
app.register_blueprint(new_blueprint)
db = DB()

@app.route("/", methods=["GET"])
def index():

    return "hello world !"
@app.route("/show_content/<id>", methods=["GET"])
def show_content(id):
    res = db.readmovie()
    return render_template("show_content.html",res = res)


if __name__ == '__main__':
    app.run(debug=True)
