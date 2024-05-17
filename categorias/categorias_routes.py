from flask import Blueprint, jsonify, request, redirect, url_for
from .categorias_model import categorias_por_id, list_categorias, categorias_existe, add_categorias, delete_categorias, update_categorias, CategoriaNaoEncontada

categorias_blueprint = Blueprint('categorias', __name__)

@categorias_blueprint.route('/categorias', methods=['GET'])
def get_categorias():
    return jsonify(list_categorias())

@categorias_blueprint.route('/categorias', methods=['POST'])
def post_categorias():
    data = request.json
    if 'nome_categoria' not in data:
        return jsonify({'erro' : 'nome da categoria não encontrado'}), 400
    id_enviado = data['id']
    if categorias_existe(id_enviado):
        return jsonify({'erro' : 'id já utlizado'}), 400
    else:
        add_categorias(data)
        return jsonify(list_categorias())

@categorias_blueprint.route('/categorias/<int:idCategorias>', methods=['DELETE'])
def remove_categorias(idCategorias):
    delete_categorias(idCategorias)
    return "removido!"

@categorias_blueprint.route('/categorias/<int:idCategorias>', methods=['PUT'])
def edit_categorias(idCategorias):
    try:
        data = request.json
        if 'nome_categoria' not in data:
            return jsonify({'erro':'nome de categoria não encontrado'}), 400
        else:
            update_categorias(idCategorias, data)
            return redirect(url_for('categorias.get_categorias', idCategorias=idCategorias))
    except CategoriaNaoEncontada:
        return jsonify({'message' : 'Erro categoria não encontrada no sistema'})

@categorias_blueprint.route('/categorias/<int:idCategorias>', methods=['DELETE', 'POST'])
def deletar_categorias(idSorvete):
        try:
            delete_categorias(idSorvete)
            return "deletado!"
        except CategoriaNaoEncontada:
            return jsonify({'message' : 'Erro, categoria não encontrado no sistema'})