from crypt import methods
from time import time
from flask import Flask, request, render_template, jsonify
from flask_pymongo import PyMongo
import bson
from datetime import datetime, timedelta
import json


app = Flask(__name__, static_url_path='/static')
app.config["MONGO_URI"] = "mongodb://localhost:27017/shop"
shop_mongo = PyMongo(app)
shop = shop_mongo.db


@app.route("/product", methods = ['POST'])
def add_product():
    product = request.get_json()
    result = shop.products.insert_one({'name': product['name'], 'price': product['price'], 'description': product['description'], 
                                       'created_at': datetime.today()})
    return str(result.inserted_id)

@app.route("/products/<product_id>")
def get_product(product_id):
    product = shop.products.find_one({'_id': bson.ObjectId(product_id)}, {'_id': False})
    print(product, type(product))
    return product

@app.route("/products/new_products")
def get_news():
    last_3_days = datetime.today() - timedelta(3)
    new_products = []
    for product in shop.products.find({'created_at': {"$gte" : last_3_days}}):
        new_products.append(product['name'])
    return str(new_products)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)