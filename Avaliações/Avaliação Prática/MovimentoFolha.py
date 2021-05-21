from TipoMovimento import TipoMovimento

class MovimentoFolha():
    def __init__(self, descrição, valor, tipo, colaborador):
        float(valor)
        self._descrição = descrição
        self._valor = valor
        self._tipo = tipo
        self._colaborador = colaborador
        
    def get_descrição(self):
        return self._descrição
    
    def get_valor(self):
        return self._valor
    
    def get_tipo(self):
        return self._tipo
    
    def set_descrição(self, descrição):
        self._descrição = descrição 
    
    def set_valor(self, valor):
        self._valor = valor
        
    def set_tipo(self, tipo):
        self._tipo = tipo
        
    def setColaborador(self, colaborador):
        self._colaborador = colaborador 
    