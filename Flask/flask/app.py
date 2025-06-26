from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the flask homepage</h1></html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return f"<html><h1>Hello {name}</h1></html>"
    return render_template("form.html")

@app.route("/submit", methods=["POST","GET"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        return f"<html><h1>Hello {name}</h1></html>"
    return render_template("form.html")

@app.route("/success/<int:score>",methods=["GET","POST"])
def sendScore(score):
    if request.method == "POST":
        return redirect(url_for("subjectform"))
    else:
        res = ""
        if score >= 50:
            res += "PASSED"
        else:
            res += "FAILED"
        return render_template("marks.html", results=[res,score])

@app.route("/marks")
def getScore():
    expr = {
                "sumeet": 99, 
                "adithya":34,
                "gokul": 98,
                "nikhil": 98,
                "charan": 100
            }
    return render_template("display.html",results = expr)

@app.route("/subjectform", methods=["POST", "GET"])
def subjectform():
    if request.method == "POST":
        physics = float(request.form['physics'])
        chemistry = float(request.form['chemistry'])
        maths = float(request.form['maths'])
        total_score = (physics+chemistry+maths)/3
        return redirect(url_for("sendScore",score=total_score))
    else:
        return render_template("subject.html")
if __name__ == "__main__":
    app.run(debug=True)