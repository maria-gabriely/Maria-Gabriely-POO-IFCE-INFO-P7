from flask import Flask
from flask_restful import Api

from controllers import ClienteControl, ClientesControl, ProdutoControl, ProdutosControl, NotaFiscalControl, NotasFiscaisControl, CalcularNotaFiscalControl, ImprimirNotaFiscalContol, ItemNotaFiscalControl, ItensNotaFiscalControl, CriarItemNotaFiscalControl

app = Flask(__name__) 
api = Api(app)

api.add_resource(ClientesControl, '/cliente')
api.add_resource(ClienteControl, '/cliente/<cliente_id>')

api.add_resource(ProdutosControl, '/produto')
api.add_resource(ProdutoControl, '/produto/<produto_id>')

api.add_resource(NotasFiscaisControl, '/notafiscal')
api.add_resource(NotaFiscalControl, '/notafiscal/<notafiscal_id>')

api.add_resource(CalcularNotaFiscalControl, '/calculanf/<notafiscal_id>')
api.add_resource(ImprimirNotaFiscalContol, '/imprimenf/<notafiscal_id>')

api.add_resource(ItemNotaFiscalControl, '/itemnf/<item_id>')
api.add_resource(ItensNotaFiscalControl, '/itensnf/<notafiscal_id>')
api.add_resource(CriarItemNotaFiscalControl, '/itemnf')

if __name__ == '__main__':
    app.run() 