from flask import Flask, request
import json
from mock_data import mock_catalog
from config import db

app = Flask("server")


@app.route("/")
def root():
    return "Hi there!"



##########################################################
#############   API CATALOG  #############################
##########################################################

@app.route("/api/about", methods=["POST"])
def about():
    me = {
        "first": "Sergio",
        "last": "Inzunza"
    }

    return json.dumps(me) # parse into json, then return




@app.route("/api/catalog")
def get_catalog():
    cursor = db.products.find({}) # get all
    all_products = []
    
    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        all_products.append(prod)

    return json.dumps(all_products)


@app.route("/api/catalog", methods=["post"])
def save_product():
    product = request.get_json()
    db.products.insert_one(product)

    print("Product saved!")
    print(product)

    #fix the _id issue
    product["_id"] = str(product["_id"])

    return json.dumps(product)



#/api/catalog/cheapest
# returns the cheapest product in the catalog
@app.route("/api/catalog/cheapest")
def get_cheapest():
    # get data from db
    cursor = db.products.find({})
    solution = cursor[0]
    for prod in cursor:
        if prod["price"] < solution["price"]:
            solution = prod

    solution["_id"] = str(solution["_id"])
    return json.dumps(solution)




#/api/catalog/total
# return the sum of all product's price
@app.route("/api/catalog/total")
def get_total():
    total = 0
    for prod in mock_catalog:
        total += prod["price"]

    return json.dumps(total)




# find a product based on the unique id
@app.route("/api/products/<id>")
def find_product(id):
    for prod in mock_catalog:
        if id == prod["_id"]:
            return json.dumps(prod)



# get the list of categories from the catalog
# /api/products/categories
# expected: a list of strings containing the unique prods categories
@app.route("/api/products/categories")
def get_categories():
    categories = []

    # push all the categories into the list
    for prod in mock_catalog:
        cat = prod["category"]
        if cat not in categories:
            categories.append(cat)

    return json.dumps(categories)



# get all the products that belong to an specified category
# /api/products/category/Fruit
@app.route("/api/products/category/<cat_name>")
def get_by_category(cat_name):
    results = []

    # add products whose category is equal to name
    for prod in mock_catalog:
        if prod["category"].lower() == cat_name.lower():
            results.append(prod)

    return json.dumps(results)




# search by text INSIDE the title
# receive a text
# return all product whose title contains the text
@app.route("/api/products/search/<text>")
def search_by_text(text):
    results = []
    text = text.lower()

    # search and add
    for prod in mock_catalog:
        title = prod["title"].lower()
        if text in title:
            results.append(prod)

    return json.dumps(results)








app.run(debug=True)

