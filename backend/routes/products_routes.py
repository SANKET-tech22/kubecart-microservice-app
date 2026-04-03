# from flask import Blueprint, jsonify
# from app.db import get_db_connection

# product_bp = Blueprint('products', __name__)

# @product_bp.route("/", methods=["GET"])
# def get_products():
#     conn = get_db_connection()
#     cur = conn.cursor()

#     cur.execute("SELECT id, name, price FROM products;")
#     products = cur.fetchall()

#     cur.close()
#     conn.close()

#     result = []
#     for p in products:
#         result.append({"id": p[0], "name": p[1], "price": p[2]})

#     return jsonify(result)


from flask import Blueprint, request, jsonify
from db import get_db_connection

product_bp = Blueprint('products', __name__)

# 🟢 GET all products
@product_bp.route("/", methods=["GET"])
def get_products():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name, price FROM products;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    products = [
        {"id": r[0], "name": r[1], "price": float(r[2])}
        for r in rows
    ]

    return jsonify(products)


# 🟢 ADD product
@product_bp.route("/", methods=["POST"])
def add_product():
    data = request.get_json()

    name = data.get("name")
    price = data.get("price")

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO products (name, price) VALUES (%s, %s) RETURNING id;",
        (name, price)
    )
    new_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({
        "id": new_id,
        "name": name,
        "price": price
    })


# 🔴 DELETE product
@product_bp.route("/<int:id>", methods=["DELETE"])
def delete_product(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM products WHERE id = %s;", (id,))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Product deleted"})