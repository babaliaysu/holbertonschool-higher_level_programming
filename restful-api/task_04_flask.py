#!/usr/bin/env python3
"""Flask ile sade RESTful API modulu."""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Istifadecileri yaddasda saxlamaq ucun luget
users = {}


@app.route("/")
def home():
    """Esas sehife ucun salamlam mətni."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Sistemdeki butun istifadeci adlarini qaytarir."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """API-nin statusunu qaytarir."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Verilmis istifadeci adina gore melumatlari qaytarir."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Yeni istifadeci elave edir."""
    # JSON-un düzgünlüyünü yoxlayiriq
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Istifadecini lugete elave edirik
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
