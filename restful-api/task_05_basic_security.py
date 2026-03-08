#!/usr/bin/env python3
"""API tehlukesizliyi: Basic Auth ve JWT modulu."""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# JWT tənzimləmələri
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # Realda daha murekkeb olmalidir
jwt = JWTManager(app)

# Istifadeci datalari (sifreler hash-lenmis formada)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# --- Basic Authentication Hissesi ---

@auth.verify_password
def verify_password(username, password):
    """Basic Auth ucun sifreni yoxlayir."""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Yalniz duzgun Basic Auth ile giris mumkundur."""
    return "Basic Auth: Access Granted"

# --- JWT Authentication Hissesi ---

@app.route('/login', methods=['POST'])
def login():
    """Login olub JWT token almaq ucun endpoint."""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    
    username = data.get("username")
    password = data.get("password")
    
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Role melumatini tokenin icine yerlesdiririk
        access_token = create_access_token(
            identity=username, 
            additional_claims={"role": user["role"]}
        )
        return jsonify(access_token=access_token)
    
    return jsonify({"error": "Bad username or password"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """Yalniz duzgun JWT token ile giris mumkundur."""
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Yalniz admin rolu olanlar ucun endpoint."""
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# --- Xeta Idareetmesi (401 qaytarmaq ucun) ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
