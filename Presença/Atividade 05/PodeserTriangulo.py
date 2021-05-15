# Se você tiver 3 canudos, possivelmente de comprimentos diferentes, pode ou não ser possível colocá-los de
# forma que formem um triângulo quando suas pontas se tocam. Por exemplo, se todos os canudos têm um 
# comprimento de 6 cm , então pode-se facilmente construir um triângulo equilátero usando-os. No entanto, 
# se um canudo tiver 15 centímetros de comprimento, enquanto os outros dois têm apenas 5 centímetros de 
# comprimento, então um triângulo não pode ser formado. Mas geralmente, se qualquer comprimento for maior
# ou igual à soma dos outros dois, os comprimentos não podem ser usados ​​para formar um triângulo. Caso 
# contrário, eles podem formar um triângulo.
#Escreva uma função que determine se três comprimentos podem ou não formar um triângulo. A função terá 3 
# parâmetros e retornará um resultado booleano. Se qualquer um dos comprimentos for menor ou igual a 0, 
# sua função deve retornar False. Caso contrário, deve determinar se os comprimentos podem ou não ser 
# usados ​​para formar um triângulo usando o método descrito no parágrafo anterior e retornar o resultado 
# apropriado. Além disso, escreva um programa que leia 3 valores inteiros de tamanhos informados do usuário
# e demonstre o comportamento de sua função.

def Triangulo (l1, l2, l3):
   #int(l1)
   #int(l2)
   #int(l3)
   triangulo = ' '
   if l1 <= 0 or l2 <=0  or l3 <= 0:
       triangulo = False
       print(triangulo)
   elif l1 >= l2 + l3 or l2 >= l1 + l3 or l3 >= l1 + l2:
       triangulo = False
       print(triangulo)
   else:
       triangulo = True
       print(triangulo)
  
print('Digite os comprimentos para saber se podem ou não formar um triângulo: ')
print('Obs: Se a resposta for False, não pode formar; se a reposta for True, pode formar')
c1 = int(input('comprimento 1: '))
c2 = int(input('comprimento 2: '))
c3 = int(input('comprimento 3: '))

Triangulo(c1,c2,c3)