import os
from flask import Flask, g, redirect, render_template, request, url_for
from src.seikei import text_to_url


app = Flask(__name__, instance_relative_config=True)


@app.route('/')
def test():
    return '<h1>this is test page<h1>'


@app.route("/gettext", methods=("GET", "POST"))
def gettext():
    if request.method == "POST":
        text = request.form["text"]

    ret_url = text_to_url(text)

    return render_template("gettext.html",url=ret_url)


app.run(host='0.0.0.0', debug=True)


