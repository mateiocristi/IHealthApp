from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename

import querries
from utils import json_response

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():  # put application's code here
    return render_template("home.html")


# @app.route("/login")
# def login():
#     if request.method == "POST":
#         username = request.form["emailInput"]
#         password = request.form["passwordInput"]



@app.route("/api-get-products/<int:category_id>/<int:supplier_id>")
@json_response
def api_get_products(category_id, supplier_id):
    products = querries.get_all_products()
    if category_id == 0:
        if supplier_id == 0:
            pass
        else:
            products = [product for product in products if product["supplier_id"] == supplier_id]
    else:
        products = querries.get_products_with_category_id(category_id)
        if supplier_id != 0:
            products = [product for product in products if product["supplier_id"] == supplier_id]
    return products


@app.route("/api-get-categories")
@json_response
def api_get_categories():
    return querries.get_all_categories()


if __name__ == '__main__':
    app.run(port=8080, debug=True)
