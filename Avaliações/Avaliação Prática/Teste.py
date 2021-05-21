from TipoMovimento import TipoMovimento
from MovimentoFolha import MovimentoFolha
from Colaborador import Colaborador
from FolhaPagamento import FolhaPagamento

def main():
   # 1.
    FP = FolhaPagamento(mes=9, ano=2019)
   # 2.
    CL01 = Colaborador(codigo=100, nome="Manoel Claudino", endereço="Av 13 de Maio 2081", telefone="88671020", bairro="Benfica", 
    cep="60020-060", cpf="124543556-89", salarioAtual=4500.00)  #a)
    CL02 = Colaborador(codigo=200, nome="Carmelina da Silva", endereço="Avenida dos Expedicionários 1200", telefone="3035-1280", bairro="Aeroporto",
    cep= "60530-020" , cpf="301789435-54", salarioAtual=2500.00)  #b)
    CL03 = Colaborador(codigo=300, nome="Gurmelina Castro Saraiva", endereço="Av João Pessoa 1020", telefone="3235-1089", bairro="Damas",
    cep= "60330-090" , cpf="350245632-76", salarioAtual=3000.00)  #c)
    
    #3.
    MF01 = MovimentoFolha(descrição = "Gratificação", valor = 4500.00, tipo = "P", colaborador = CL01) #a)
    MF02 = MovimentoFolha(descrição = "Plano Saúde", valor = 1000.00, tipo = "P", colaborador = CL01) #b)
    MF03 = MovimentoFolha(descrição = "Pensão", valor = 600.00, tipo = "D", colaborador = CL01) #c)
    MF04 = MovimentoFolha(descrição = "Gratificação", valor = 2500.00, tipo = "P", colaborador = CL02) #d)
    MF05 = MovimentoFolha(descrição = "Gratificação", valor = 1000.00, tipo = "P", colaborador = CL02) #e)
    MF06 = MovimentoFolha(descrição = "Faltas", valor = 600.00, tipo = "D", colaborador = CL02) #f)
    MF07 = MovimentoFolha(descrição = "Gratificação", valor = 4500.00, tipo = "P", colaborador = CL03) #g) 
    MF08 = MovimentoFolha(descrição = "Plano Saúde", valor = 1000.00, tipo = "P", colaborador = CL03) #h) 
    MF09 = MovimentoFolha(descrição = "Pensão", valor = 600.00, tipo = "D", colaborador = CL03) #i) 
    
    #6.
    FP.inserirMovimentos(MF01)
    FP.inserirMovimentos(MF02)
    FP.inserirMovimentos(MF03)
    FP.inserirMovimentos(MF04)
    FP.inserirMovimentos(MF05)
    FP.inserirMovimentos(MF06)
    FP.inserirMovimentos(MF07)
    FP.inserirMovimentos(MF08)
    FP.inserirMovimentos(MF09)
    
    # 7.
    CL01.inserirMovimentos(MF01)
    CL01.inserirMovimentos(MF02)
    CL01.inserirMovimentos(MF03)
    
    CL02.inserirMovimentos(MF04)
    CL02.inserirMovimentos(MF05)
    CL02.inserirMovimentos(MF06)
    
    CL03.inserirMovimentos(MF07)
    CL03.inserirMovimentos(MF08)
    CL03.inserirMovimentos(MF09)
    
    FP.inserirColaboradores(CL01)
    FP.inserirColaboradores(CL02)
    FP.inserirColaboradores(CL03)
    
    print("Resultado da Folha de Pagamento: \n", FP.calcularFolha())
    
    print("\nInformações do trabalhador de", CL01.calcularSalario())
    print("\nInformações do trabalhador de", CL02.calcularSalario())
    print("\nInformações do trabalhador de", CL03.calcularSalario())

if __name__ == '__main__':
    main()
