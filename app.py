from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from utils import json_response

app = Flask(__name__)


@app.route("/home")
def home():  # put application's code here
    return render_template("home.html")


@app.route("/api-get-products/<int: category_id>/<int: supplier_id>")
@json_response
def api_get_products(category_id, supplier_id):
    product_1 = {"id": 1, "name": "product_1", "description": "some desc", "stock": 2, "default_price": 100.00,
                "actual_price": 100.00, "rating": 2, "category_id": 1, "supplier_id": 2, "img_path": ""}
    product_2 = {"id": 1, "name": "product_1", "description": "some desc", "stock": 2, "default_price": 100.00,
                "actual_price": 100.00, "rating": 2, "category_id": 1, "supplier_id": 2, "img_path": ""}
    products = []

    if category_id == 0:
        if supplier_id == 0:
            products = querries.get_all_products()
        else:
            products = [product for product in products if product["supplier_id"] == supplier_id]
    else:
        products = querries.get_products_with_category_id(category_id)
        if supplier_id != 0:
            products = [product for product in products if product["supplier_id"] == supplier_id]
    return products


@app.route('/api-get-categories')
@json_response
def api_get_categories():
    return querries.get_all_categories()


if __name__ == '__main__':
    app.run(port=8080, debug=True)
