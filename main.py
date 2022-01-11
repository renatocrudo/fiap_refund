from flask import Flask, json, jsonify, request
from flask_pydantic_spec import FlaskPydanticSpec
import game_controller
from db import create_tables

app = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='Refund API')
spec.register(app)

@app.route('/refunds', methods=["GET"])
def get_refunds():
    games = game_controller.get_games()
    return jsonify(games)

@app.route("/refund", methods=["POST"])
def insert_refund():
    game_details = request.get_json()
    name = game_details["name"]
    price = game_details["price"]
    rate = game_details["rate"]
    result = game_controller.insert_game(name, price, rate)
    return jsonify(result)

@app.route("/refund", methods=["PUT"])
def update_refund():
    game_details = request.get_json()
    id = game_details["id"]
    name = game_details["name"]
    price = game_details["price"]
    rate = game_details["rate"]
    result = game_controller.update_game(id, name, price, rate)
    return jsonify(result)

@app.route("/refund/<id>", methods=["DELETE"])
def delete_refund(id):
    result = game_controller.delete_game(id)
    return jsonify(result)

@app.route("/refund/<id>", methods=["GET"])
def get_refund_by_id(id):
    game = game_controller.get_by_id(id)
    return jsonify(game)


# Habilitando CORS
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

if __name__ == "__main__":
    create_tables()
    app.run()