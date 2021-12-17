from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
import cryptography as cy

import cryptography
import querries
from utils import json_response

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():  # put application's code here
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["email"]
        password = request.form["password"]
        try:
            user = querries.get_user_by_username(username)
            if username == user["username"] or username == user["email"] and cy.verify_password(password, user["password"]):
                return redirect(url_for("home"))
            else:
                return render_template("login.html", message="Invalid login")
        except:
            return render_template("login.html", message="Invalid login")
    return render_template("login.html", message=None)


@app.route("/register", methods=["GET", "POST"])
def register():
    username = request.form["username"]
    first_name = request.form["firstName"]
    last_name = request.form["lastName"]
    email = request.form["email"]
    address = request.form["address"]
    county = request.form["county"]
    city = request.form["city"]
    phone = request.form["phone"]
    birthdate = request.form["birthdate"]
    cnp = request.form["cnp"]
    password = request.form["password"]
    password_confirm = request.form["confirmPassword"]
    if password != password_confirm:
        return render_template(url_for("register"))
    if not querries.get_user_by_username(username) and len(username) > 5 and len(password) > 5:
        password = cy.hash_password(password)
        if querries.add_user(username, email, password, first_name, last_name, county, city, address, phone, birthdate, cnp) == "ok":
            session.update({"username": username})
            session.update({"user_id": querries.get_user_by_username(username)["id"]})
        return redirect(url_for("home"))
    return render_template("register.html")



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
