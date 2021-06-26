from enum import unique
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

from sqlalchemy.orm import backref

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:**************@localhost/cliente'

db = SQLAlchemy(app)

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(40), nullable = False)
    codigo = db.Column(db.Integer, unique = True)
    cnpjcpf = db.Column(db.String(40), unique = True)
    tipocliente = db.Column(db.String(20), nullable = False)
    
    def to_json(self): # transforma os objetos em json
        return { "id": self.id, "nome": self.nome, "codigo": self.codigo, "cnpj/cpf": self.cnpjcpf, "tipocliente": self.tipocliente}

""" CONTROLLERS """


@app.route("/")
def index():
    T = """ MENU : 
    /clientes -> para ver todos os clientes                                    método: GET
    /cliente/id -> para consultar um cliente de acordo com o seu id            método: GET
    /cadastro -> para cadastrar um novo cliente                                método: POST
    /atualizacliente/id -> para atualizar um cliente de acordo com o seu id    método: PUT
    /deletarcliente/id -> para deletar um cliente de acordo com o seu id       método: DELETE"""
    return T

# seleciona todos os clientes
@app.route("/clientes", methods = ["GET"]) 
def seleciona_clientes():
    clientes_objetos = Cliente.query.all() # recebe os clientes
    clientes_json = [cliente.to_json() for cliente in clientes_objetos]
    
    return response(200, "Clientes", clientes_json)

# seleciona apenas um cliente pelo seu id
@app.route("/cliente/<id>", methods = ["GET"])
def seleciona_cliente(id):
    cliente_objeto = Cliente.query.filter_by(id = id).first() # filtra cliente pelo seu id 
    cliente_json = cliente_objeto.to_json()
    
    return response(200, "Cliente", cliente_json)

# cadastra cliente
@app.route("/cadastro", methods = ["POST"])
def cadastra_cliente():
    body = request.get_json()
    
    try:
        cliente = Cliente(nome = body["nome"], codigo = body["codigo"], cnpjcpf = body["cnpj/cpf"], tipocliente = body["tipocliente"])
        db.session.add(cliente)
        db.session.commit()
        
        return response(201, "Novo Cliente", cliente.to_json(), "Cadastrado com Sucesso!")
    
    except Exception as e:
        print(e)
        return response(400, "Novo Cliente", {}, "Erro ao Cadastrar")
    
# atualiza cliente
@app.route("/atualizacliente/<id>", methods = ["PUT"]) #PUT é o padrão de atualização
def atualiza_cliente(id):
    cliente_objeto = Cliente.query.filter_by(id = id).first()
    body = request.get_json()
    
    try:
        if("nome" in body):
            cliente_objeto.nome = body["nome"]
        if("codigo" in body):
            cliente_objeto.codigo = body["codigo"]
        if("cnpj/cpf" in body):
            cliente_objeto.cnpjcpf = body["cnpj/cpf"]
        if("tipocliente" in body):
            cliente_objeto.tipocliente = body["tipocliente"]
        
        db.session.add(cliente_objeto)
        db.session.commit()
        
        return response(200, "Atualização de Cliente", cliente_objeto.to_json(), "Atualizado com Sucesso!")
    
    except Exception as e:
        print(e)
        return response(400, "Atualização de Cliente", {}, "Erro ao Atualizar")
    
# Deleta cliente
@app.route("/deletarcliente/<id>", methods = ["DELETE"])
def deleta_cliente(id):
    cliente_objeto = Cliente.query.filter_by(id = id).first()
    
    try:
        db.session.delete(cliente_objeto)
        db.session.commit()
        
        return response(200, "Deletar Cliente", cliente_objeto.to_json(), "Deletado com Sucesso!")
    
    except Exception as e:
        print(e)
        return response(400, "Deletar Cliente", {}, "Erro ao Deletar")
        
def response(status, nome_conteudo, conteudo, mensagem = False):
    body = {}
    body[nome_conteudo] = conteudo
    
    if (mensagem): # se a mensagem não for False
        body["mensagem"] = mensagem
    
    return Response(json.dumps(body), status=status)

app.run()