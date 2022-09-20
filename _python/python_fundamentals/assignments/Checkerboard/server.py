from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def checkerBoard8():
    return render_template("Index.html")


# @app.route("/4")
# def checkerBoard4():
#     return render_template("Index.html")


if __name__ == "__main__":
    app.run(debug=True)
