from flask import Flask
app=Flask("__name__")

@app.route ("/")
def hello():
    return "Hello World!"

@app.route ("/dojo")
def dojo():
    return "Dojo!"

@app.route ("/say/<name>")
def name(name):
    return "Hi "+name

@app.route ("/repeat/<int:id>/<name1>")
def repeat(id,name1):
    return (name1*id)

@app.errorhandler(404)
def error(e):
    return ("Sorry! No response. Try again")

if __name__ == "__main__":
    app.run(debug=True) 