from flask import Flask, escape, render_template, request, redirect
from grab import who_next 
from main import stats, teams, icons
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html", stats=stats, teams=teams, icons= icons)

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)