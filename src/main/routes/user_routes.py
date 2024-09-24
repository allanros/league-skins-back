from flask import Blueprint, jsonify, request
from src.main.http_types.http_request import HttpRequest

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/user", methods=["POST"])
def create_user():
    # http_request = HttpRequest(body=request.json)

    return jsonify({"message": "User created"}), 201

@user_routes.route("/user", methods=["GET"])
def get_user():
    http_request = HttpRequest(headers=request.headers)
    user_id = http_request.headers.get('User-ID')

    return jsonify({"message": f"{user_id}"}), 200
