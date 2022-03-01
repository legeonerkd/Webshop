from flask import Flask, request, render_template
from flask_pymongo import PyMongo
import json
import flask


app = Flask(__name__, static_url_path='/static')
app.config["MONGO_URI"] = "mongodb://27017:27017/shop"
shop = PyMongo(app)
shop_db = shop.db


@app.route("/add_article")
def add_artecle():
    shop_db.articles.insert_one({'name': "todo title", 'price': "todo body", 'description': ""})
    return flask.jsonify(message="success")