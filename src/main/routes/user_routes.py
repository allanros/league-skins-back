from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request
from src.main.http_types.http_request import HttpRequest

from src.main.composer.user_register_composer import user_register_composer
from src.main.composer.user_finder_composer import user_finder_composer
from src.main.composer.user_updater_composer import user_updater_composer
from src.main.composer.user_add_skin_composer import user_add_skin_composer
from src.main.composer.user_login_composer import user_login_composer

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/user/register", methods=["POST"])
def create_user():
    use_case = user_register_composer()
    http_request = HttpRequest(body=request.json)

    response = use_case.register(http_request)

    return jsonify(response.body), response.status_code

@user_routes.route("/user", methods=["GET"])
@jwt_required()
def get_user():
    use_case = user_finder_composer()
    http_request = HttpRequest(headers=request.headers)

    response = use_case.find(http_request)

    return jsonify(response.body), response.status_code

@user_routes.route("/user", methods=["PATCH"])
def update_user():
    use_case = user_updater_composer()
    http_request = HttpRequest(headers=request.headers, body=request.json)

    response = use_case.update(http_request)

    return jsonify(response.body), response.status_code

@user_routes.route("/user/skin", methods=["PATCH"])
@jwt_required()
def add_user_skin():
    use_case = user_add_skin_composer()
    http_request = HttpRequest(headers=request.headers, body=request.json)

    response = use_case.add(http_request)

    return jsonify(response.body), response.status_code

@user_routes.route("/user/login", methods=["POST"])
def login():
    use_case = user_login_composer()
    http_request = HttpRequest(body=request.json)

    response = use_case.login(http_request)

    return jsonify(response.body), response.status_code

@user_routes.route("/user/get_id", methods=["GET"])
@jwt_required()
def get_id():
    current_user_id = get_jwt_identity()
    return jsonify(user_id=current_user_id), 200
