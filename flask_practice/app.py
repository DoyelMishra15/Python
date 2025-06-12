from flask import Flask

app = Flask(__name__)

@app.route('/potato')
def welcome():
    return "This is my first Flask app"

@app.route('/')
def wroot():
    return "This is my root Flask app"

@app.route('/bob')
def bob():
    return "This is bob Flask app"

app.run()