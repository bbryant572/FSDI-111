from flask import Flask


app = Flask(__name__)


@app.route("/")
def about_me():
    me = {
        "first_name": "Brett",
        "last_name": "Bryant",
        "hobbies": "Darts",
        "active": True
    }
    return me


@app.route("/greet/<fname>/<lname>")
def greet_user(fname, lname):
    return "<h1>Hello, %s %s</h1>" % (fname, lname)


@app.route("/square/<int:num>/")
def square_num(num):
    return "<h1>%s squared is: %s</h1>" % (num, num*num)
