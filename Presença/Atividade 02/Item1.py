# Criar uma lista em Python para implementar as seguintes Estruturas de Dados:
# 1) Pilha (inserir e retirar pelo topo da Pilha. Considerar o topo como sendo o índice 0 da Lista.
# 2) Fila (Inserir no final da Fila. Considerar o final da fila o elemento de maior índice positivo. Retirar da Fila pelo elemento do inicio da Lista que tem o índice 0.)
# 3) Lista Encadeada (A retirada e a inserção de elementos se faz em qualquer posição da Lista). Usar os métodos da Lista Python que fazem menção nos seus parâmetros a índices.

Lista1 = [1,2,5,6,9]
print(Lista1)
x = 2
Lista1.insert(0,x)
print(Lista1)

Lista1.pop(0)
print(Lista1)
