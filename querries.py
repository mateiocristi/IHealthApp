import connection


@connection.connection_handler
def get_user_by_email(cursor, email):
    querry = """SELECT * 
                FROM users
                WHERE email = %(email)s;"""
    cursor.execute(querry, {"email": email})
    return cursor.fetchone()


@connection.connection_handler
def get_user_by_id(cursor, user_id):
    querry = """SELECT * 
                FROM users
                WHERE id = %(user_id)s;"""
    cursor.execute(querry, {"user_id": user_id})
    return cursor.fetchone()


@connection.connection_handler
def get_all_products(cursor):
    querry = """SELECT *
                FROM products;"""
    cursor.execute(querry)
    return cursor.fetchall()


@connection.connection_handler
def get_products_by_category(cursor, category_id):
    querry = """SELECT *
                FROM products
                WHERE category_id = %(category_id)s;"""
    cursor.execute(querry, {"category_id": category_id})
    return cursor.fetchall()


@connection.connection_handler
def get_products_by_supplier(cursor, supplier_id):
    querry = """SELECT *
                FROM products
                WHERE supplier_id = %(supplier_id)s;"""
    cursor.execute(querry, {"supplier_id": supplier_id})
    return cursor.fetchall()


@connection.connection_handler
def get_product_by_id(cursor, product_id):
    querry = """SELECT *
                FROM products
                WHERE id = %(product_id)s;"""
    cursor.execute(querry, {"product_id": product_id})
    return cursor.fetchone()


@connection.connection_handler
def get_all_categories(cursor):
    querry = """SELECT *
                FROM categories;"""
    cursor.execute(querry)
    return cursor.fetchall()


@connection.connection_handler
def add_cart(cursor):
    querry = """INSERT INTO carts (quantity_product_id) VALUES ('') RETURNING id;"""
    cursor.execute(querry)
    return cursor.fetchone()


@connection.connection_handler
def add_user(cursor, user):
    cart_id = add_cart()
    print(cart_id)
    user.update({"cart_id": cart_id["id"]})
    querry = """INSERT INTO users 
                (first_name, last_name, county, city, address, birth_date, email, phone_number, password, cart_id)
                VALUES (%(first_name)s,
                %(last_name)s,
                %(county)s,
                %(city)s,
                %(address)s,
                %(birth_date)s,
                %(email)s,
                %(phone_number)s,
                %(password)s,
                %(cart_id)s);"""
    cursor.execute(querry, user)


@connection.connection_handler
def get_cart_products(cursor, cart_id):
    querry = """SELECT quantity_product_id FROM carts WHERE id = %(cart_id)s;"""
    cursor.execute(querry, {"cart_id": cart_id})
    return cursor.fetchone()


@connection.connection_handler
def update_cart(cursor, user, product_id, quantity):
    cart = f"{get_cart_products()['quantity_product_id']},{quantity}_{product_id}"
    querry = """UPDATE carts 
                SET quantity_product_id = %(cart)s
                WHERE id=%(cart_id)s;"""
    user.update({"cart": cart})
    cursor.execute(querry, user)
