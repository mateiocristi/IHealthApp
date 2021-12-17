import connection


@connection.connection_handler
def get_user_by_username(cursor, username):
    querry = """
        SELECT * 
        FROM users
        WHERE 
            username = %(username)s
        OR
            email = %(username)s
        
            ;"""
    cursor.execute(querry, {'username': username})
    return cursor.fetchone()


@connection.connection_handler
def get_user_by_id(cursor, user_id):
    querry = """
        SELECT * 
        FROM users
        WHERE id = %(user_id)s
            ;"""
    cursor.execute(querry, {'user_id': user_id})
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
def get_products_by_id(cursor, product_id):
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




