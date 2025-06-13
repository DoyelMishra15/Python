from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/potato')
def welcome():
    return "This is my first Flask app"

@app.route('/')
def wroot():
    return "This is my root Flask app"

@app.route('/bob')
def bob():
    return render_template("index.html")

@app.route('/method',methods=['GET','POST'])
def method():
    if request.method=='POST':
        return "Post request"
    else:
        return "maybe using a Get request"

app.run()