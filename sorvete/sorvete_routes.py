from flask import Blueprint, jsonify, request
from .sorvete_model import sorvete_por_id, list_sorvete, sorvete_existe, add_sorvete, delete_sorvete, update_sorvete, SorveteNaoEncontrado

sorvetes_blueprint = Blueprint('sorvete', __name__)

@sorvetes_blueprint.route('/sorvetes', methods=['GET'])
def get_sorvetes():
    return jsonify(list_sorvete())

@sorvetes_blueprint.route('/sorvetes', methods=['POST'])
def post_sorvetes():
    data = request.json
    if 'sabor' not in data:
        return jsonify({'erro' : 'sabor não encontrado'}), 400
    id_enviado = data['id']
    if sorvete_existe(id_enviado):
        return jsonify({'erro' : 'id já utlizado'}), 400
    else:
        add_sorvete(data)
        return jsonify(list_sorvete())

@sorvetes_blueprint.route('/sorvetes/<int:idSorvete>', methods=['DELETE'])
def remove_sorvete(idSorvete):
    delete_sorvete(idSorvete)
    return "removido!"

@sorvetes_blueprint.route('/sorvetes/<int:idSorvete>', methods=['PUT'])
def edit_sorvete(idSorvete):
    try:
        data = request.json
        if 'sabor' not in data:
            return jsonify({'erro':'sabor de sorvete não encontrado'}), 400
        else:
            update_sorvete(idSorvete, data)
            return jsonify({'ok':f'sorvete alterado para {data['sabor'], data['categoria'], data['preco'], data['qntd_estoque']}'})
    except SorveteNaoEncontrado:
        return jsonify({'message' : 'Erro sorvete não encontrado no sistema'})

@sorvetes_blueprint.route('/sorvetes/<int:idSorvete>', methods=['DELETE', 'POST'])
def deletar_sorvete(idSorvete):
        try:
            delete_sorvete(idSorvete)
            return "deletado!"
        except SorveteNaoEncontrado:
            return jsonify({'message' : 'Erro, sorvete não encontrado no sistema'})