from flask import Blueprint, jsonify
from app.db import get_db_connection

product_bp = Blueprint('products', __name__)

@product_bp.route("/", methods=["GET"])
def get_products():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name, price FROM products;")
    products = cur.fetchall()

    cur.close()
    conn.close()

    result = []
    for p in products:
        result.append({"id": p[0], "name": p[1], "price": p[2]})

    return jsonify(result)