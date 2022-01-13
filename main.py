from flask import Flask, json, jsonify, request
import requests
from flask_pydantic_spec import FlaskPydanticSpec
import refund_controller
from db import create_tables

app = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='Refund API')
spec.register(app)

@app.route('/refunds', methods=["GET"])
def get_refunds():
    recibo = refund_controller.get_recibo()
    #games = game_controller.get_games()
    return jsonify(recibo)

@app.route("/refund", methods=["POST"])
def insert_refund():
    recibo_details = request.get_json()
    cnpj = recibo_details["cnpj"]
    nome_estabelecimento = recibo_details["nome_estabelecimento"]
    descricao = recibo_details["descricao"]
    total = recibo_details["total"]
    imagem = recibo_details["imagem"]
    url_api = "http://localhost:6000/read_ocr"
    response = requests.post(url = url_api, json={'foto_recibo':imagem})
    texto = response.content.decode()
    print(response.content)
    result = refund_controller.insert_recibo(cnpj, nome_estabelecimento, descricao, total, imagem)
    
    return jsonify(texto)

@app.route("/refund", methods=["PUT"])
def update_refund():
    recibo_details = request.get_json()
    cnpj = recibo_details["cnpj"]
    nome_estabelecimento = recibo_details["nome_estabelecimento"]
    descricao = recibo_details["descricao"]
    total = recibo_details["total"]
    imagem = recibo_details["imagem"]
    result = refund_controller.update_recibo(id, cnpj, nome_estabelecimento, descricao, total, imagem)
    return jsonify(result)

@app.route("/refund/<id>", methods=["DELETE"])
def delete_refund(id):
    result = refund_controller.delete_recibo(id)
    return jsonify(result)

@app.route("/refund/<id>", methods=["GET"])
def get_refund_by_id(id):
    recibo = refund_controller.get_by_id(id)
    return jsonify(recibo)



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