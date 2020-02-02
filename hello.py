from flask import Flask, escape, request
from grab import who_next 
from main import url_points 

app = Flask(__name__)

@app.route('/')
def hello():

    stat = who_next(url_points, 'points')
    name = request.args.get("name", "World")
    return f'Lebron has {escape(stat)} career points!'