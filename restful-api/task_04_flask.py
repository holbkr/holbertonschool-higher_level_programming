#!/usr/bin/python3
"""This module is using flask to run a local server. It's using a virtual
environment, to do tests. It manages some endpoints and permits to store, adds
and retrieve users data"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!", 200


@app.route("/data", methods=["GET"])
def data():
    users_list = list(users.keys())
    return jsonify(users_list), 200


@app.route("/status", methods=["GET"])
def status():
    return "OK", 200


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    search_user = users.get(username)
    if search_user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(search_user), 200


@app.route("/add_user", methods=["POST"])
def add_user():
    new_user = request.get_json(silent=True) or {}

    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # ✅ вот это нужно для теста duplicate username
    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run()
