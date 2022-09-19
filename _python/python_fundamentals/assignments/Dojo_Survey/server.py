import re
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def dojoSurvey():
    return render_template("Index.html")


@app.route("/result", methods=['POST'])
def result():
    print(request.form)
    name_from_form = request.form['name']
    lacation_from_form = request.form['location']
    language_from_form = request.form['language']
    comment_from_form = request.form['comment']
    return render_template("result.html", name_on_template=name_from_form,
                           location_on_template=lacation_from_form,
                           language_on_template=language_from_form,
                           comment_on_template=comment_from_form)


if __name__ == "__main__":
    app.run(debug=True, port=9000)
