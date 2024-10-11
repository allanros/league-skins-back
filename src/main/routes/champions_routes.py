from flask import Blueprint, jsonify, request
from src.main.http_types.http_request import HttpRequest

from src.main.composer.champion_cache_updater import champion_cache_updater_composer
# from src.main.composer.champion_register_composer import champion_register_composer
from src.main.composer.champion_finder_composer import champion_finder_composer
from src.main.composer.champion_updater_composer import champion_updater_composer

champions_routes = Blueprint("champions_routes", __name__)

@champions_routes.route("/champions", methods=["GET"])
def get_champions():
    use_case = champion_finder_composer()

    response = use_case.find_all()

    return jsonify(response.body), response.status_code

@champions_routes.route("/champions/<champion_name>", methods=["GET"])
def get_one_champion(champion_name: str):
    use_case = champion_finder_composer()
    http_request = HttpRequest(body={"champion": champion_name})

    response = use_case.find(http_request)

    return jsonify(response.body), response.status_code

# @champions_routes.route("/champions", methods=["POST"])
# def create_champion():
#     use_case = champion_register_composer()
#     http_request = HttpRequest(body=request.json)

#     response = use_case.register(http_request)

#     return jsonify(response.body), response.status_code

@champions_routes.route("/champions/cache", methods=["GET"])
def champion_update_cache():
    use_case = champion_cache_updater_composer()

    response = use_case.update_cache()

    return jsonify(response.body), response.status_code


@champions_routes.route("/champions", methods=["PATCH"])
def update_champion():
    use_case = champion_updater_composer()
    http_request = HttpRequest(body=request.json)

    response = use_case.update(http_request)

    return jsonify(response.body), response.status_code
