import json
from app import db

from sqlalchemy.orm import backref

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(40), nullable = False)
    codigo = db.Column(db.Integer, unique = True)
    cnpjcpf = db.Column(db.String(40), unique = True)
    tipocliente = db.Column(db.String(20), nullable = False)
    
    def to_json(self): # transforma os objetos em json
        return { "id": self.id, "nome": self.nome, "codigo": self.codigo, "cnpj/cpf": self.cnpjcpf, "tipocliente": self.tipocliente}
    
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    codigo = db.Column(db.Integer, unique = True)
    descricao = db.Column(db.String(50), nullable = False)
    valorUnitario = db.Column(db.Float, nullable = False)
    
    def to_json(self): # transforma os objetos em json
        return { "id": self.id, "código": self.codigo, "descrição": self.descricao, "valor unitário": self.valorUnitario}

class Itemnf(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    sequencial = db.Column(db.Integer, nullable = False)
    quantidade = db.Column(db.Integer, nullable = False)
    id_produto = db.Column(db.Integer, db.ForeignKey('produto.id'))
    Produto = db.relationship('Produto', foreign_keys= id_produto)

    def to_json(self): # transforma os objetos em json
        return { "id": self.id, "sequencial": self.sequencial, "quantidade": self.quantidade, "produto": self.id_produto}

    
class NotaFiscal(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    codigo = db.Column(db.Integer, unique = True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    Cliente = db.relationship('Cliente', foreign_keys= id_cliente)
    valornota = db.Column(db.Float, nullable = False)
    id_itemnotafiscal = db.Column(db.Integer, db.ForeignKey('itemnf.id'))
    ItemNotaFiscal = db.relationship('Itemnf', foreign_keys= id_itemnotafiscal)
    
    def to_json(self): # transforma os objetos em json
        return { "id": self.id, "código": self.codigo, "Cliente": self.id_cliente, "Valor Nota": self.valornota, "Produtos": self.id_produto}
    
db.create_all()
    
    