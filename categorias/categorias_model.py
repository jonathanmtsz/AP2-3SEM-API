from config import db

class Categorias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_categoria = db.Column(db.String)

    def __init__(self, nome_categoria):
        self.nome_categoria = nome_categoria
    
    def to_dict(self):
        return{'id' : self.id, 'nome_categoria' : self.nome_categoria}
    
class CategoriaNaoEncontada(Exception):
    pass

def categorias_por_id(categorias_id):
    categorias = Categorias.query.get(categorias_id)
    if not categorias:
        raise CategoriaNaoEncontada
    return categorias.to_dict()

def list_categorias():
    categoriass = Categorias.query.all()
    return [categorias.to_dict() for categorias in categoriass]

def categorias_existe(categorias_id):
    try:
        categorias_por_id(categorias_id)
        return True
    except CategoriaNaoEncontada:
        return False
    
def add_categorias(categorias_novo):
    novo = Categorias(nome_categoria=categorias_novo['nome_categoria'])
    db.session.add(novo)
    db.session.commit()

def delete_categorias(categorias_id):
    categorias = Categorias.query.get(categorias_id)
    if not categorias:
        raise CategoriaNaoEncontada
    db.session.delete(categorias)
    db.session.commit()

def update_categorias(categorias_id, categorias_novo):
    categorias = Categorias.query.get(categorias_id)
    if not categorias:
        raise CategoriaNaoEncontada
    categorias.nome_categoria = categorias_novo['nome_categoria']
    db.session.commit()

