from flask import Blueprint, request, jsonify

order_bp = Blueprint('orders', __name__)

orders = []

@order_bp.route("/", methods=["POST"])
def create_order():
    data = request.json
    order = {
        "id": len(orders) + 1,
        "product_id": data.get("product_id"),
        "quantity": data.get("quantity")
    }
    orders.append(order)
    return jsonify(order), 201