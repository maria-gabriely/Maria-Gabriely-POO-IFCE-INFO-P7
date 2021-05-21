from MovimentoFolha import MovimentoFolha
from Colaborador import Colaborador

class FolhaPagamento():
    def __init__ (self, mes, ano):
        int(mes)
        int(ano)
        
        self._mes = mes
        self._ano = ano
        self._Movimentos = []
        self._Colaboradores = []
        
    def get_mes(self):
        return self._mes
    
    def get_ano(self):
        return self._ano
    
    def set_mes(self, mes):
        self._mes = mes       
        
    def set_ano(self, ano):
        self._ano = ano
        
    def inserirMovimentos(self, movimentofolha): #4.
        if isinstance(movimentofolha, MovimentoFolha):
            self._Movimentos.append(movimentofolha)
    
    def inserirColaboradores(self, colaborador):
        if isinstance(colaborador, Colaborador):
            self._Colaboradores.append(colaborador)
            print(self._Colaboradores)   
        
    def calcularFolha(self): #8
        TotalSalários = 0.0
        TotaldeProventos = 0.0
        TotaldeDescontos = 0.0
        for colaborador in self._Colaboradores:
            TotalSalários = TotalSalários +  colaborador._salarioAtual
            
        for movimentofolha in self._Movimentos:
            if movimentofolha._tipo == "P":
                TotaldeProventos = TotaldeProventos +  movimentofolha._valor
        
        for movimentofolha in self._Movimentos:
            if movimentofolha._tipo == "D":
                TotaldeDescontos =  TotaldeDescontos + movimentofolha._valor     
        
        Total_a_pagar = (TotalSalários + TotaldeProventos) - TotaldeDescontos
        
        string = "Total de Salários = R$ {0}, Total de Proventos = R${1}, Total de Descontos = R${2}, Total a Pagar = R${3}".format(TotalSalários, TotaldeProventos, TotaldeDescontos, Total_a_pagar)
        return string
        
    