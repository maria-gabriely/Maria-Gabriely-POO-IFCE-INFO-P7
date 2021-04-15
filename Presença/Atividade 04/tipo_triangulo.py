# O triângulo pode ser classificado com base no comprimento de seus lados em 
# equilátero, isósceles ou escaleno. Todos os três lados de um triângulo 
# equilátero têm o mesmo comprimento. Um triângulo isósceles tem dois lados que 
# são do mesmo comprimento e um terceiro lado que é diferente comprimento. Se 
# todos os lados tiverem comprimentos diferentes, o triângulo é escaleno. Escreva
#  um programa que leia os comprimentos dos três lados de um triângulo do 
# usuário. Em seguida, exiba uma mensagem que declara o tipo do triângulo.
print ('Digite os valores dos lados do triângulo para saber a sua classificação:')
l1 = int (input('lado 1: '))
l2 = int (input('lado 2: '))
l3 = int (input('lado 3: '))

if l1 == l2 and l3 == l1 :
    print('Triângulo Equilátero')
elif l1 == l2 and l1 != l3 or l2 == l3 and l2 != l1 or l3 == l1 and l3 != l2:
    print('Triângulo Isósceles')
else:
    print('Triângulo Escaleno')

    

