from MovimentoFolha import MovimentoFolha 

class Colaborador():
    def __init__(self, codigo, nome, endereço, telefone, bairro, cep, cpf, salarioAtual):
        int(codigo)
        float(salarioAtual)
        
        self._codigo = codigo
        self._nome = nome
        self._endereço = endereço
        self._telefone = telefone
        self._bairro = bairro
        self._cep = cep
        self._cpf = cpf
        self._salarioAtual = salarioAtual
        self._Movimentos = []
    
    def get_codigo(self):
        return self._codigo
    
    def get_nome(self):
        return self._nome
    
    def get_endereço(self):
        return self._endereço
    
    def get_telefone(self):
        return self._telefone
    
    def get_bairro(self):
        return self._bairro
    
    def get_cep(self):
        return self._cep
    
    def get_cpf(self):
        return self._cpf
    
    def get_slarioAtual(self):
        return self._salarioAtual
    
    def set_codigo(self, codigo):
        self._codigo = codigo 
    
    def set_nome(self, nome):
        self._nome = nome
        
    def set_endereço(self, endereço):
        self._endereço = endereço
        
    def set_telefone(self, telefone):
        self._telefone = telefone
        
    def set_bairro(self, bairro):
        self._bairro = bairro
        
    def set_cep(self, cep):
        self._cep = cep
        
    def set_cpf(self, cpf):
        self._cpf = cpf
        
    def set_salarioAtual(self, salarioAtual):
        self._salarioAtual = salarioAtual
    
    def inserirMovimentos(self, movimentofolha): #5)
        if isinstance(movimentofolha, MovimentoFolha):
            self._Movimentos.append(movimentofolha)
     
    def calcularSalario(self): #9.
        TotalProventos = 0.0
        TotalDescontos = 0.0
        for movimentofolha in self._Movimentos:
           if movimentofolha._tipo == "P":
                TotalProventos += movimentofolha._valor
        
        for movimentofolha in self._Movimentos:
           if movimentofolha._tipo == "D":
                TotalDescontos += movimentofolha._valor     
        
        Valor_a_Receber = (self._salarioAtual + TotalProventos) - TotalDescontos
                  
        string = "Código: {0}, Nome: {1}\n  Salário: R$ {2}, Total de Proventos: R$ {3}, Total de Descontos: R$ {4}, Valor Líquido a Receber: R$ {5}".format(self._codigo, self._nome, self._salarioAtual, TotalProventos,
         TotalDescontos, Valor_a_Receber) 

        return string
        
