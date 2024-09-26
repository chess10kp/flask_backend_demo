# type: ignore
from flask import Flask
from flask import render_template, request
from setup_db import (
    insert,
    view,
    delete,
)

app = Flask(__name__)


@app.route("/")
def call_this_function_anything_you_want():
    return "<h1>This is some HTML!</h1>"


@app.route("/page")
def return_a_html_page():
    return render_template("index.html")


@app.route("/page/<any>")
def variables_as_query_parameters(any):
    return render_template("index.html", any=any)


@app.route("/send_data", methods=["POST"])
def send_data():
    data = request.form["data"]
    return data

@app.route("/bookmarks", methods=["GET"])
def get_all_bookmarks():
    return view()

@app.route("/bookmarks", methods=["POST"])
def add_bookmark():
    pass


@app.route("/bookmarks/<string:bookmark>", methods=["DELETE"])
def delete_bookmark(bookmark):
    delete(bookmark)

app.run()
