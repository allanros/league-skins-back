from flask import Blueprint, jsonify

champions_routes = Blueprint("champions_routes", __name__)

@champions_routes.route("/champions", methods=["GET"])
def get_champions():
    return jsonify({"message": "Champions"}), 200

@champions_routes.route("/champions/<champion_name>", methods=["GET"])
def get_one_champion(champion_name: str):
    return jsonify({"message": f"{champion_name}"}), 200
