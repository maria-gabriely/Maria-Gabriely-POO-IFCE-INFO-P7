from enum import unique
from tables import Cliente, Produto, Itemnf, NotaFiscal
from app import app
from app import db
from flask import Flask, Response, request
import json 

""" Controllers"""

""" Clientes """
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
@app.route("/cadastrarcliente", methods = ["POST"])
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
        
""" --------------------------------------------------------------------------------------------------------------"""

""" Produtos"""
# seleciona todos os produtos
@app.route("/produtos", methods = ["GET"]) 
def seleciona_produtos():
    produtos_objetos = Produto.query.all() # recebe os produtos
    produtos_json = [produto.to_json() for produto in produtos_objetos]
    
    return response(200, "Produtos", produtos_json)

# seleciona apenas um produto pelo seu id
@app.route("/produto/<id>", methods = ["GET"])
def seleciona_produto(id):
    produto_objeto = Produto.query.filter_by(id = id).first() # filtra produto pelo seu id 
    produto_json = produto_objeto.to_json()
    
    return response(200, "Produto", produto_json)

# cadastra produto
@app.route("/cadastrarproduto", methods = ["POST"])
def cadastra_produto():
    body = request.get_json()
    
    try:
        produto = Produto(codigo = body["codigo"], descricao = body["descrição"], valorUnitario = body["valor unitário"])
        db.session.add(produto)
        db.session.commit()
        
        return response(201, "Novo produto", produto.to_json(), "Cadastrado com Sucesso!")
    
    except Exception as e:
        print(e)
        return response(400, "Novo produto", {}, "Erro ao Cadastrar")
    
# atualiza produto
@app.route("/atualizarproduto/<id>", methods = ["PUT"]) 
def atualiza_produto(id):
    produto_objeto = Produto.query.filter_by(id = id).first()
    body = request.get_json()
    
    try:
        if("codigo" in body):
            produto_objeto.codigo = body["codigo"]
        if("descrição" in body):
            produto_objeto.descricao = body["descrição"]
        if("valor Unitário" in body):
            produto_objeto.valorUnitario = body["valor unitário"]
        
        db.session.add(produto_objeto)
        db.session.commit()
        
        return response(200, "Atualização de produto", produto_objeto.to_json(), "Atualizado com Sucesso!")
    
    except Exception as e:
        print(e)
        return response(400, "Atualização de produto", {}, "Erro ao Atualizar")
    
# Deleta produto
@app.route("/deletarproduto/<id>", methods = ["DELETE"])
def deleta_produto(id):
    produto_objeto = Produto.query.filter_by(id = id).first()
    
    try:
        db.session.delete(produto_objeto)
        db.session.commit()
        
        return response(200, "Deletar produto", produto_objeto.to_json(), "Deletado com Sucesso!")
    
    except Exception as e:
        print(e)
        return response(400, "Deletar produto", {}, "Erro ao Deletar")
    
""" -----------------------------------------------------------------------------------------------------------------------------------"""

""" Item Nota Fiscal """
# Ler todos os itens 
@app.route("/itens", methods = ["GET"]) 
def seleciona_itens():
    itemnf_objetos = Itemnf.query.all() # recebe os itens
    itemnf_json = [item.to_json() for item in itemnf_objetos]
    
    return response(200, "Itens da Nota Fiscal", itemnf_json)

# seleciona apenas um item pelo seu id
@app.route("/item/<id>", methods = ["GET"])
def seleciona_item(id):
    itemnf_objeto = Itemnf.query.filter_by(id = id).first() # filtra item pelo seu id 
    itemnf_json = itemnf_objeto.to_json()
    
    return response(200, "Item da Nota Fiscal", itemnf_json)

# cadastra item
@app.route("/cadastraritem", methods = ["POST"])
def cadastra_item():
    body = request.get_json()
    
    try:
        item = Itemnf(sequencial = body["sequencial"], quantidade = body["quantidade"], id_produto = body["produto"])
        db.session.add(item)
        db.session.commit()
        
        return response(201, "Novo Item", item.to_json(), "Cadastrado com Sucesso!")
    
    except Exception as e:
        print(e)
        return response(400, "Novo Item", {}, "Erro ao Cadastrar")
    
# atualiza item
@app.route("/atualizaitem/<id>", methods = ["PUT"]) 
def atualiza_item(id):
    itemnf_objeto = Itemnf.query.filter_by(id = id).first()
    body = request.get_json()
    
    try:
        if("sequencial" in body):
            itemnf_objeto.sequencial = body["sequencial"]
        if("quantidade" in body):
            itemnf_objeto.quantidade = body["quantidade"]
        if("produto" in body):
            itemnf_objeto.id_produto = body["produto"]
        
        db.session.add(itemnf_objeto)
        db.session.commit()
        
        return response(200, "Atualização de Item", itemnf_objeto.to_json(), "Atualizado com Sucesso!")
    
    except Exception as e:
        print(e)
        return response(400, "Atualização de Item", {}, "Erro ao Atualizar")
    
# Deleta item
@app.route("/deletaritem/<id>", methods = ["DELETE"])
def deleta_item(id):
    itemnf_objeto = Itemnf.query.filter_by(id = id).first()
    
    try:
        db.session.delete(itemnf_objeto)
        db.session.commit()
        
        return response(200, "Deletar Item", itemnf_objeto.to_json(), "Deletado com Sucesso!")
    
    except Exception as e:
        print(e)
        return response(400, "Deletar Item", {}, "Erro ao Deletar")
    
""" ------------------------------------------------------------------------------------------------------------------------"""
""" Nota Fiscal"""

# Ler todas as notas fiscais 
@app.route("/notasfiscais", methods = ["GET"]) 
def seleciona_notas():
    notas_objetos = NotaFiscal.query.all() # recebe as notas fiscais
    notas_json = [nota.to_json() for nota in notas_objetos]
    
    return response(200, "Notas Fiscais", notas_json)

# seleciona apenas uma nota fiscal pelo seu id
@app.route("/notafiscal/<id>", methods = ["GET"])
def seleciona_nota(id):
    nota_objeto = NotaFiscal.query.filter_by(id = id).first() # filtra item pelo seu id 
    nota_json = nota_objeto.to_json()
    
    return response(200, "Nota Fiscal", nota_json)

# cadastra nota
@app.route("/cadastrarnotafiscal", methods = ["POST"])
def cadastra_notafiscal():
    body = request.get_json()
    
    try:
        nota = NotaFiscal(codigo = body["codigo"], id_cliente = body["cliente"], valornota = body["valor nota"], id_itemnotafiscal = body["item da nota fiscal"])
        db.session.add(nota)
        db.session.commit()
        
        return response(201, "Nova Nota Fiscal", nota.to_json(), "Cadastrada com Sucesso!")
    
    except Exception as e:
        print(e)
        return response(400, "Nova Nota Fiscal", {}, "Erro ao Cadastrar")
    
# atualiza nota
@app.route("/atualizarnotafiscal/<id>", methods = ["PUT"]) 
def atualiza_nota(id):
    nota_objeto = NotaFiscal.query.filter_by(id = id).first()
    body = request.get_json()
    
    try:
        if("codigo" in body):
            nota_objeto.codigo = body["codigo"]
        if("cliente" in body):
            nota_objeto.id_cliente = body["cliente"]
        if("valor nota" in body):
            nota_objeto.valornota = body["valor nota"]
        if("item da nota fiscal" in body):
            nota_objeto.id_itemnotafiscal = body["item da nota fiscal"]
        
        db.session.add(nota_objeto)
        db.session.commit()
        
        return response(200, "Atualização de Nota Fiscal", nota_objeto.to_json(), "Atualizada com Sucesso!")
    
    except Exception as e:
        print(e)
        return response(400, "Atualização de Nota Fiscal", {}, "Erro ao Atualizar")
    
# Deleta nota fiscal
@app.route("/deletarinotafiscal/<id>", methods = ["DELETE"])
def deleta_nota(id):
    nota_objeto = NotaFiscal.query.filter_by(id = id).first()
    
    try:
        db.session.delete(nota_objeto)
        db.session.commit()
        
        return response(200, "Deletar Nota Fiscal", nota_objeto.to_json(), "Deletada com Sucesso!")
    
    except Exception as e:
        print(e)
        return response(400, "Deletar Nota Fiscal", {}, "Erro ao Deletar")
""" ----------------------------------------------------------------------------------------------------------------------------------"""    
def response(status, nome_conteudo, conteudo, mensagem = False):
    body = {}
    body[nome_conteudo] = conteudo
    
    if (mensagem): # se a mensagem não for False
        body["mensagem"] = mensagem
    
    return Response(json.dumps(body), status=status)


if __name__ == "__main__":
    app.run()



