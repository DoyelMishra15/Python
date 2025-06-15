from flask import Flask, request, render_template

f = Flask(__name__)

@f.route('/potato')
def welcome():
    return "This is my first Flask app"

@f.route('/')
def wroot():
    return render_template("index.html")

@f.route('/bob')
def bob():
    return "This is bob Flask app"

@f.route('/method',methods=['GET','POST'])
def method():
    if request.method=='POST':
        return "Post request"
    else:
        return "maybe using a Get request"

f.run()