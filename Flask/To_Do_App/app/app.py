import os
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
MONGO_URI = os.environ.get("uri")
client = MongoClient(MONGO_URI)
db = client['PYTHON_PROJECTS']  # Replace with your database name
collection = db["TO_DO_LIST"]

@app.route("/addTask/",methods=["POST"])
def addTask(tasks):
    collection.insert_one({'Name': tasks})
    return redirect(url_for("index"))
        
@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        task = request.form["task"]
        collection.insert_one({'Name': task})
        expr =  f"Added task {task} to the list"
        return render_template("index.html", results=[collection,expr])
    else:
        return render_template("index.html", results=[collection,""])

if __name__ == "__main__":
    app.run(debug=True)