import connection


@connection.connection_handler
def get_user_by_email(cursor, email):
    querry = """
        SELECT * 
        FROM users
        WHERE email = %(email)s
        
            ;"""
    cursor.execute(querry, {"email": email})
    return cursor.fetchone()


@connection.connection_handler
def get_user_by_id(cursor, user_id):
    querry = """
        SELECT * 
        FROM users
        WHERE id = %(user_id)s
            ;"""
    cursor.execute(querry, {"user_id": user_id})
    return cursor.fetchone()


@connection.connection_handler
def get_all_products(cursor):
    querry = """
            SELECT *
            FROM products
            ;"""
    cursor.execute(querry)
    return cursor.fetchall()


@connection.connection_handler
def get_products_by_category(cursor, category_id):
    querry = """
                SELECT *
                FROM products
                WHERE category_id = %(category_id)s
                ;"""
    cursor.execute(querry, {"category_id": category_id})
    return cursor.fetchall()


@connection.connection_handler
def get_products_by_supplier(cursor, supplier_id):
    querry = """
                SELECT *
                FROM products
                WHERE supplier_id = %(supplier_id)s
                ;"""
    cursor.execute(querry, {"supplier_id": supplier_id})
    return cursor.fetchall()


@connection.connection_handler
def get_product_by_id(cursor, product_id):
    querry = """
                SELECT *
                FROM products
                WHERE id = %(product_id)s
                ;"""
    cursor.execute(querry, {"product_id": product_id})
    return cursor.fetchone()


@connection.connection_handler
def get_all_categories(cursor):
    querry = """
                SELECT *
                FROM categories
                ;"""
    cursor.execute(querry)
    return cursor.fetchall()


@connection.connection_handler
def add_cart(cursor):
    querry = """
        INSERT INTO carts (id) VALUES (default) RETURNING id
            ;"""
    cursor.execute(querry)
    return cursor.fetchone()


@connection.connection_handler
def add_user(cursor, user):
    cart_id = add_cart()
    user.update({"cart_id": cart_id["id"]})
    querry = """
        INSERT INTO users 
        (first_name, last_name, county, city, address, birth_date, email, phone_number, password, cart_id)
        VALUES (
        %(first_name)s,
        %(last_name)s,
        %(county)s,
        %(city)s,
        %(address)s,
        %(birth_date)s,
        %(email)s,
        %(phone_number)s,
        %(password)s,
        %(cart_id)s
        )
        RETURNING 'ok' as message
            ;"""
    cursor.execute(querry, user)
    return cursor.fetchone()


@connection.connection_handler
def get_all_orders(cursor):
    querry = """
        SELECT * FROM orders
            ;"""
    cursor.execute(querry)
    return cursor.fetchall()


@connection.connection_handler
def get_order_by_id(cursor, order_id):
    querry = """
        SELECT * FROM orders WHERE id = %(id)s
            ;"""
    cursor.execute(querry, {"id": order_id})
    return cursor.fetchall()


@connection.connection_handler
def get_order_by_user_id(cursor, user_id):
    querry = """
        SELECT * FROM orders WHERE user_id = %(user_id)s
            ;"""
    cursor.execute(querry, {"user_id": user_id})
    return cursor.fetchall()


@connection.connection_handler
def get_all_cart_products_for_cart(cursor, cart_id):
    querry = """
            SELECT * FROM cart_products WHERE cart_id = %(cart_id)s
                ;"""
    cursor.execute(querry, {"cart_id": cart_id})
    return cursor.fetchall()


@connection.connection_handler
def get_cart_product_for_cart_by_product_id(cursor, cart_id, product_id):
    querry = """
            SELECT * FROM cart_products WHERE cart_id = %(cart_id)s AND product_id = %(product_id)s
                ;"""
    cursor.execute(querry, {"cart_id": cart_id, "product_id": product_id})
    return cursor.fetchone()


@connection.connection_handler
def delete_all_cart_products_by_cart_id(cursor, cart_id):
    querry = """
        DELETE FROM cart_products WHERE cart_id = %(cart_id)s
            ;"""
    cursor.execute(querry, {"cart_id": cart_id})


@connection.connection_handler
def delete_cart_products_by_cart_id_and_product_id(cursor, cart_id, product_id):
    querry = """
            DELETE FROM cart_products WHERE cart_id = %(cart_id)s AND product_id = %(product_id)s
                ;"""
    cursor.execute(querry, {"cart_id": cart_id, "product_id": product_id})


@connection.connection_handler
def update_cart(cursor, user, product_id, quantity):
    actual_product_quantity = get_cart_product_for_cart_by_product_id(
        user["cart_id"], product_id
    )
    if actual_product_quantity:
        quantity += int(actual_product_quantity["quantity"])
        delete_cart_products_by_cart_id_and_product_id(user["cart_id"], product_id)
    querry = """
        INSERT INTO cart_products VALUES 
        (
            %(product_id)s,
            %(quantity)s,
            %(cart_id)s
        )
            ;"""
    cursor.execute(
        querry,
        {"product_id": product_id, "quantity": quantity, "user_id": user["user_id"]},
    )


@connection.connection_handler
def get_order_products_by_order_id(cursor, order_id):
    querry = """
        SELECT * FROM order_products WHERE order_id = %(order_id)s
            ;"""
    cursor.execute(querry, {"order_id": order_id})
    return cursor.fetchall()


@connection.connection_handler
def get_all_orders_by_user_id(cursor, user):
    querry = """
        SELECT * FROM orders WHERE user_id = %(user_id)s
            ;"""
    cursor.execute(querry, {"user_id": user["id"]})
    return cursor.fetchall()


@connection.connection_handler
def insert_order(cursor, user, payment_type):
    querry = """
        INSERT INTO orders (payment_type, user_id) VALUES 
        (
        %(payment_type)s,
        %(user_id)s
        )
        RETURNING id
            ;"""
    cursor.execute(querry, {"payment_type": payment_type, "user_id": user["id"]})
    return cursor.fetchone()


# @connection.connection_handler
# def insert_products