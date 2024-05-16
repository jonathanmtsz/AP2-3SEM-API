from config import db

class Sorvete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sabor = db.Column(db.String)
    categoria = db.Column(db.String)
    preco = db.Column(db.Float)
    qntd_estoque = db.Column(db.Integer)

    def __init__(self, sabor, categoria, preco, qntd_estoque):
        self.sabor = sabor
        self.categoria = categoria
        self.preco = preco
        self.qntd_estoque = qntd_estoque
    
    def to_dict(self):
        return{'id' : self.id, 'sabor' : self.sabor, 'categoria' : self.categoria, 'preco' : self.preco, 'qntd_estoque' : self.qntd_estoque}

class SorveteNaoEncontrado(Exception):
    pass

def sorvete_por_id(sorvete_id):
    sorvete = Sorvete.query.get(sorvete_id)
    if not sorvete:
        raise SorveteNaoEncontrado
    return sorvete.to_dict()

def list_sorvete():
    sorvetes = Sorvete.query.all()
    return [sorvete.to_dict() for sorvete in sorvetes]

def sorvete_existe(sorvete_id):
    try:
        sorvete_por_id(sorvete_id)
        return True
    except SorveteNaoEncontrado:
        return False
    
def add_sorvete(sorvete_novo):
    novo = Sorvete(sabor = sorvete_novo['sabor'], categoria = sorvete_novo['categoria'], preco = sorvete_novo['preco'], qntd_estoque = sorvete_novo['qntd_estoque'])
    db.session.add(novo)
    db.session.commit()

def delete_sorvete(sorvete_id):
    sorvete = Sorvete.query.get(sorvete_id)
    if not sorvete:
        raise SorveteNaoEncontrado
    db.session.delete(sorvete)
    db.session.commit()

def update_sorvete(sorvete_id, sorvete_novo):
    sorvete = Sorvete.query.get(sorvete_id)
    if not sorvete:
        raise SorveteNaoEncontrado
    sorvete.sabor = sorvete_novo['sabor']
    sorvete.categoria = sorvete_novo['categoria']
    sorvete.preco = sorvete_novo['preco']
    sorvete.qntd_estoque = sorvete_novo['qntd_estoque']
    db.session.commit()

