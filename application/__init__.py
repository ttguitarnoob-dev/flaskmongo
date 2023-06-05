from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["SECRET_KEY"] = "cb8c0481ed58bc152b47ff1c0ce5594d9c754472"
app.config["MONGO_URI"] = "mongodb+srv://tthompson:Bungfodder123@cluster0.hxddmni.mongodb.net/?retryWrites=true&w=majority"

#setup mongodb
mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes