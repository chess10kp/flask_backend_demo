# type: ignore

# imports
from flask import Flask
from flask import render_template, request
from setup_db import (
    view_by_url,
)
import sqlite3

app = Flask(__name__)

# define a route (in this case, http://localhost:5003/ )
@app.route("/")
def call_this_function_anything_you_want():
    return "<h1>This is some HTML!</h1>"

# you can also return a HTML page
@app.route("/page")
def return_a_html_page():
    return render_template("index.html")


@app.route("/page/<any>")
def variables_as_path_parameters(any):
    return render_template("index.html", any=any)

# http://localhost:5003/send_data?data=hello -> returns "hello"
@app.route("/send_data", methods=["GET"])
def send_data_with_query_parameters():
    data = request.args.get("data")
    return data 

# learn SQL at https://www.sqltutorial.org/sql-syntax/
@app.route("/create_db", methods=["POST"])
def create_db():
    conn = sqlite3.connect("new.db")
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS sample_db (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
        )
        """
    )
    conn.commit()
    conn.close()
    return "Database created"

# http://localhost:5003/insert_data?first_name=john&last_name=doe -> returns "Data inserted"
@app.route("/insert_data", methods=["POST"])
def insert_names():
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")

    conn = sqlite3.connect("new.db")
    cur = conn.cursor()
    cur.execute(
        f"""
        INSERT INTO sample_db (first_name, last_name)
        VALUES ({first_name}, {last_name})
        """
    )
    conn.commit()
    conn.close()
    return "Data inserted"



# http://localhost:5003/bookmarks?id=0
@app.route("/bookmarks", methods=["GET"])
def check_answer():
    id = request.args.get("id")
    return view_by_url(id)



# TODO: endpoint GET "/calculate"
# Handles 
# 1. http://localhost:5003/calculate/add/10/20 - returns 30
# 2. http://localhost:5003/calculate/sub/10/20 - returns -10

# TODO: endpoint POST "/hello"
# Handles json input
# FORMATTING IS IMPORTANT! Your output must look exactly like this
# 1. http://localhost:5003/ - returns "Hello John, you are 25 years old" 
# request-body {
#   "name": "John",
#   "age": 25
# }

# To test:
# 1. Windows: ./test_windows.exe
# 2. MacOS: ./test_mac
# 3. Linux: ./test_linux

# if you get a code, then make a request with the "/bookmarks" endpoint for a special surprise


app.run(port=5003)
