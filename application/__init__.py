from flask import Flask, request
# from mongoengine import Document, StringField, IntField
from pymongo import MongoClient


app = Flask(__name__)

#mongodb connection
client = MongoClient('mongodb://127.0.0.1:27017')
db = client['poodb']
collection = db['pooclection']





from application import routes