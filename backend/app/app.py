from flask import Flask
from flask_cors import CORS
from routes.products_routes import product_bp
from routes.orders_routes import order_bp

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
# Register routes
app.register_blueprint(product_bp, url_prefix="/products")
app.register_blueprint(order_bp, url_prefix="/orders")

@app.route("/")
def home():
    return {"message": "KubeCart Backend Running 🚀"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)