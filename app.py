from flask import Flask, render_template, request, redirect, url_for, session, flash
import cryptography as cy

import querries
from utils import json_response

app = Flask(__name__)
app.secret_key = b'_5#y2x"F4Qdu\n\xec]/'


@app.route("/")
@app.route("/home")
def home():  # put application's code here
    if "username" in session:
        username = session["username"]
        user_id = session["user_id"]
        return render_template(
            "home.html",
            username=username,
            user_id=user_id
        )
    return render_template("home.html", username=None)


@app.route("/user-profile/<user_id>")
def user_route(user_id):
    if "username" in session:
        username = session["username"]
        user_id = user_id
        return render_template(
            "user_profile.html",
            username=username,
            user_id=user_id
        )
    return render_template("home.html", username=None)


@app.route("/login", methods=["GET"])
def display_login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_user():
    email = request.form["email"]
    password = request.form["password"]
    user = querries.get_user_by_email(email)
    if user is not None and cy.verify_password(password, user["password"]):
        session['username'] = user["email"]
        session['user_id'] = querries.get_user_by_email(user["email"])["id"]
        return redirect(url_for("home"))
    else:
        flash('Username and/ or password are wrong')
        return render_template("login.html")


@app.route("/logout")
def logout_user():
    session.pop('username', None)
    session.pop('user_id', None)
    return redirect(url_for('home'))


@app.route("/register", methods=["GET"])
def display_register():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register_user():
    user = {"first_name": request.form["firstName"],
            "last_name": request.form["lastName"],
            "email": request.form["email"],
            "address": request.form["address"],
            "county": request.form["county"],
            "city": request.form["city"],
            "phone_number": request.form["phone"],
            "birth_date": request.form["birthdate"],
            "password": request.form["password"]}
    if user["password"] != request.form["confirmPassword"]:
        flash('Please submit matching passwords')
        return redirect(url_for("display_register"))
    if querries.get_user_by_email(user["email"]) and len(user["email"]) < 5 and len(user["password"]) < 5:
        return redirect(url_for("display_register"))
    hashed_password = cy.hash_password(user["password"])
    user["password"] = hashed_password
    querries.add_user(user)
    return redirect(url_for("home"))


@app.route("/api-get-products/<int:category_id>/<int:supplier_id>")
@json_response
def api_get_products(category_id, supplier_id):
    products = querries.get_all_products()
    if category_id == 0:
        if supplier_id == 0:
            pass
        else:
            products = [
                product for product in products if product["supplier_id"] == supplier_id
            ]
    else:
        products = querries.get_products_with_category_id(category_id)
        if supplier_id != 0:
            products = [
                product for product in products if product["supplier_id"] == supplier_id
            ]
    return products


@app.route("/api-get-categories")
@json_response
def api_get_categories():
    return querries.get_all_categories()


if __name__ == "__main__":
    app.run(port=8080, debug=True)
