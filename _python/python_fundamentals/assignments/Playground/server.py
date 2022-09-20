from os import times
from flask import Flask, render_template

playground_app = Flask(__name__)


@playground_app.route("/play")
def play():
    return render_template("Index3.html", num_box=3, color_box="blue")


@playground_app.route("/play/<times>")
def numbers_box(times):
    return render_template("Index3.html", num_box=int(times), color_box="blue")


@playground_app.route("/play/<times>/<color_cahnge>")
def colorCange(times, color_cahnge):
    return render_template("Index3.html", num_box=int(times), color_box=color_cahnge)


if __name__ == "__main__":
    playground_app.run(debug=True)
