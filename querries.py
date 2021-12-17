import connection


@connection.connection_handler
def get_all_products(cursor):
    querry = """
            SELECT *
            FROM products
            ;"""
    cursor.execute(querry)
    return cursor.fetchall()


@connection.connection_handler
def get_products_with_category_id(cursor, category_id):
    querry = """
                SELECT *
                FROM products
                WHERE category_id = %(category_id)s
                ;"""
    cursor.execute(querry, {"category_id": category_id})
    return cursor.fetchall()


@connection.connection_handler
def get_all_categories(cursor):
    querry = """
                SELECT *
                FROM categories
                ;"""
    cursor.execute(querry)
    return cursor.fetchall()
