# Para ganhar o prêmio máximo na Mega Sena, é necessário
#acertar todos os 6 números em seu bilhete com os 6 números entre 1 e 60
#sorteados. Escreva um programa que gere uma seleção aleatória de 6 números para
#uma aposta. Certifique-se de que os 6 números selecionados não contenham
#duplicatas. Exibir os números em ordem crescente.
import random
num = random.sample(range(1,61),6)
ordem_num = [int(val) for val in num]
print('Seus números para a aposta: ', sorted(ordem_num))