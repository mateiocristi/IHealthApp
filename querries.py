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
        {"product_id": product_id, "quantity": quantity, "cart_id": user["cart_id"]},
    )


@connection.connection_handler
def get_cart_products_for_user(cursor, user):
    querry = """
        SELECT * FROM cart_products,products WHERE cart_id=%(cart_id)s AND cart_products.product_id=products.id
        ;"""
    cursor.execute(querry, user)
    return cursor.fetchall()


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


@connection.connection_handler
def insert_order_products(cursor, products, order_id):
    querry = """
        INSERT INTO order_products (product_id, quantity, order_id)  
        VALUES
        (
            %(product_id)s,
            %(quantity)s,
            %(order_id)s
        )
            ;"""
    for product in products:
        cursor.execute(
            querry,
            {
                "product_id": product["product_id"],
                "quantity": product["quantity"],
                "order_id": order_id,
            },
        )


def place_order(user, payment_type):
    order_id = insert_order(user, payment_type)["id"]
    products = get_all_cart_products_for_cart(user["cart_id"])
    insert_order_products(products, order_id)
    delete_all_cart_products_by_cart_id(user["cart_id"])


@connection.connection_handler
def get_all_suppliers(cursor):
    querry = """
        SELECT * FROM suppliers
            ;"""
    cursor.execute(querry)
    return cursor.fetchall()


@connection.connection_handler
def insert_supplier(cursor, supplier):
    querry = """
        INSERT INTO suppliers ( name, description, phone_number, email, website) VALUES
        (
            %(name)s,
            %(description)s,
            %(phone_number)s,
            %(email)s,
            %(website)s
        ) 
            ;"""
    cursor.execute(querry, supplier)


@connection.connection_handler
def search_in_products(cursor, search_term):
    querry = """
        SELECT * FROM products 
        WHERE 
                name LIKE %(search_term)s
            OR
                description LIKE %(search_term)s
            ;"""
    cursor.execute(querry, {"search_term": f"%{search_term}%"})
    return cursor.fetchall()


@connection.connection_handler
def search_in_categories(cursor, search_term):
    querry = """
        SELECT * FROM categories
        WHERE
                name LIKE %(search_term)s
            OR
                description LIKE %(search_term)s
            ;"""
    cursor.execute(querry, {"search_term": f"%{search_term}%"})
    return cursor.fetchall()


@connection.connection_handler
def search_in_suppliers(cursor, search_term):
    querry = """
        SELECT * FROM suppliers
        WHERE
                name LIKE %(search_term)s
            OR
                description LIKE %(search_term)s
            ;"""
    cursor.execute(querry, {"search_term": f"%{search_term}%"})
    return cursor.fetchall()


def search(search_term):
    products = search_in_products(search_term)
    categories = search_in_categories(search_term)
    suppliers = search_in_suppliers(search_term)
    return products, categories, suppliers


@connection.connection_handler
def get_sales(cursor):
    querry = """
        SELECT id, name, description, stock, default_price, actual_price, rating, category_id, supplier_id, 
        (default_price-products.actual_price) as sale FROM products ORDER BY sale DESC LIMIT 3
            ;"""
    cursor.execute(querry)
    return cursor.fetchall()
