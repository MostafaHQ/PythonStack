from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def checkerBoard8():
    return render_template("Index.html", x=8, y=4, color_one="black", color_two="red")


@app.route("/<x>")
def checkerBoardx(x):
    return render_template("Index.html", x=int(x), y=4, color_one="black", color_two="red")


@app.route("/<x>/<y>")
def checkerBoardxy(x, y):
    return render_template("Index.html", x=int(x), y=int(y), color_one="black", color_two="red")


# @app.route("/<x>/<y>/<color1>/<color2>")
# def checkerBoardxyColoring(x, y, color1, color2):
#     return render_template("Index.html", x=int(x), y=int(y), color_one=color1, color_two=color2)


if __name__ == "__main__":
    app.run(debug=True)
