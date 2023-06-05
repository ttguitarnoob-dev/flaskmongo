from application import app, collection
from flask import request

@app.route("/", methods = ["GET"])
def index():
    data = collection.find()
    return data

@app.route("/add", methods = ['POST'])
def add():
    name = request.form.get('name')
    age = request.form.get('age')
    data = {'name': name, 'age': age}
    collection.insert_one(data)