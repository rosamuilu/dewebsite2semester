from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/newyork.html")
def newyork():
    return render_template("newyork.html")

@app.route("/losangeles.html")
def losangeles():
    return render_template("losangeles.html")

@app.route("/chicago.html")
def chicago():
    return render_template("chicago.html")

@app.route("/houston.html")
def houston():
    return render_template("houston.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True) 