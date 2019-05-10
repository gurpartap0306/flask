from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return renter_template("index.html")
