"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
import datetime
from cliente        import Cliente
from produto        import Produto
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal():       
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente = cliente
        self._nome = self._cliente.get_nome()
        self._cnpjcpf = self._cliente.get_cnpjcpf() 
        self._data=datetime.datetime.now()   
        self._itens=[]
        self._valorNota=0.0
 
    
    def setCliente(self, cliente):
        self._cliente=cliente    
            
    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
        
    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor = valor + item._valorItem
        self.valorNota=valor
     
    def imprimirNotaFiscal(self):
        print('-' * 82)
        print('NOTA FISCAL', str(self._data).rjust(70))
        print('Cliente: {0}    Nome: {1}'.format(self._Id, self._nome))
        print('CPF/CNPJ: ', self._cnpjcpf)
        print('-' * 82)
        print('ITENS')
        print('-' * 82)
        print('%1s %18s %25s %15s %15s' % ('SEQ ', 'DESCRIÇÃO', 'QTD', 'VALOR UNIT', 'PREÇO'))
        print('%1s %28s %16s %14s %16s' % ('-' * 4, '-' * 20, '-' * 5, '-' * 11, '-' * 6))
        for item in self._itens:
            print(repr(item._sequencial).ljust(13), str(item._descricao).ljust(23), str(item._quantidade).rjust(10), str(item._valorUnitario).rjust(12), repr(item._valorItem).rjust(19))
        print('_' * 82)
        print('Valor Total: ', self.valorNota)
        return print()