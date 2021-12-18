from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
import cryptography as cy

import querries
from utils.json_response import json_response

app = Flask(__name__)
app.secret_key = b'_5#y2x"F4Qdu\n\xec]/'


@app.route("/")
@app.route("/home")
def home():  # put application's code here
    categories = querries.get_all_categories()
    suppliers = querries.get_all_suppliers()
    if "email" in session:
        email = session["email"]
        user_id = session["user_id"]
        return render_template("home.html", email=email, user_id=user_id, categories=categories, suppliers=suppliers)
    return render_template("home.html", email=None, categories=categories, suppliers=suppliers)


@app.route("/user_profile/<user_id>")
def user_route(user_id):
    categories = querries.get_all_categories()
    suppliers = querries.get_all_suppliers()
    if "email" in session:
        email = session["email"]
        user_id = user_id
        return render_template("user_profile.html", email=email, user_id=user_id)
    return render_template("home.html", email=None, categories=categories, suppliers=suppliers)


@app.route("/login", methods=["GET", "POST"])
def login():
    categories = querries.get_all_categories()
    suppliers = querries.get_all_suppliers()
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        try:
            print("try ok")
            user = querries.get_user_by_email(email)
            if email == user["email"] and cy.verify_password(
                password, user["password"]
            ):
                print("login ok")
                session.update({"email": email, "user_id": user["id"]})
                return redirect(url_for("home", email=email, categories=categories, suppliers=suppliers))
            else:
                return render_template("login.html", message="Invalid login")
        except:
            return render_template("login.html", message="Invalid login")
    return render_template("login.html", message=None)


@app.route("/register", methods=["GET", "POST"])
def register():
    categories = querries.get_all_categories()
    suppliers = querries.get_all_suppliers()
    if request.method == "POST":
        user = {
            "first_name": request.form["firstName"],
            "last_name": request.form["lastName"],
            "email": request.form["email"],
            "address": request.form["address"],
            "county": request.form["county"],
            "city": request.form["city"],
            "phone_number": request.form["phone"],
            "birth_date": request.form["birthdate"],
            "password": request.form["password"],
        }
        password_confirm = request.form["confirmPassword"]
        if user["password"] != password_confirm:
            return render_template(url_for("register"))
        print("password ok")
        if (
            not querries.get_user_by_email(user["email"])
            and len(user["email"]) > 5
            and len(user["password"]) > 5
        ):
            print("user ok")
            user["password"] = cy.hash_password(user["password"])
            resp = querries.add_user(user)["message"]
            print("response: " + resp)
            if resp == "ok":
                session.update({"email": user["email"]})
                session.update(
                    {"user_id": querries.get_user_by_email(user["email"])["id"]}
                )
        return redirect(url_for("home", categories=categories, suppliers=suppliers))
    return render_template("register.html")


@app.route("/search")
def search():
    search_term = request.args["search"]
    products, categories, suppliers = querries.search(search_term)
    return render_template('')


@app.route("/logout")
def logout():
    categories = querries.get_all_categories()
    suppliers = querries.get_all_suppliers()
    # remove the username from the session if it's there
    session.pop("email", None)
    session.pop("user_id", None)
    return redirect(url_for("home", categories=categories, suppliers=suppliers))


@app.route("/cart")
def cart_route():
    if not session["user_id"]:
        categories = querries.get_all_categories()
        suppliers = querries.get_all_suppliers()
        return redirect(url_for("home", categories=categories, suppliers=suppliers))
    user = querries.get_user_by_id(session["user_id"])
    print("cart_id {}", user["cart_id"])
    products = querries.get_cart_products_for_user(user)
    total = 0
    for product in products:
        if product["quantity"] > 0:
            total += product["quantity"] * product["actual_price"]
    return render_template("cart.html", products=products, total=total)


@app.route("/checkout", methods=["POST", "GET"])
def checkout_route():
    total = request.args["total"]
    if request.method == "POST":
        categories = querries.get_all_categories()
        suppliers = querries.get_all_suppliers()
        if not session["user_id"]:
            return redirect(url_for("home"))
            # handle checkout
        return redirect(url_for("home", email=session["email"], user_id=session["user_id"], categories=categories, suppliers=suppliers))
    user = querries.get_user_by_id(session["user_id"])
    return render_template("checkout.html", user_id=user["id"], email=user["email"], total=total)


@app.route("/product/<product_id>")
def product_route(product_id):
    product = querries.get_product_by_id(product_id)
    img_path = f"/static/images/product_{product_id}.jpg"
    return render_template("product.html", product=product, img_path=img_path)


@app.route("/api_get_products/<int:category_id>/<int:supplier_id>")
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
        products = querries.get_products_by_category(category_id)
        if supplier_id != 0:
            products = [
                product for product in products if product["supplier_id"] == supplier_id
            ]
    return products


@app.route("/api_get_categories")
@json_response
def api_get_categories():
    return querries.get_all_categories()


@app.route("/api_get_suppliers")
@json_response
def api_get_suppliers():
    return querries.get_all_suppliers()


@app.route("/api_get_cart")
@json_response
def api_get_cart():
    user_id = session["user_id"]
    user = querries.get_user_by_id(user_id)
    cart_products = querries.get_all_cart_products_for_cart(user["cart_id"])
    return cart_products


@app.route("/api_update_cart/<int:product_id>/<int:quantity>", methods=["PUT"])
@json_response
def api_update_cart(product_id, quantity):
    print("updating cart")
    user = querries.get_user_by_id(session["user_id"])
    querries.update_cart(user, product_id, quantity)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
