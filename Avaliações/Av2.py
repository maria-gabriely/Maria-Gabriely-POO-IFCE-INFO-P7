# O código Morse é um esquema de codificação que usa travessões e pontos para 
# representar dígitos e letras. Nesta atividade, você escreverá um programa que 
# usa um dicionário para armazenar o mapeamento desses símbolos para o código 
# Morse. Use um ponto para representar um ponto e um hífen para representar um 
# travessão.Seu programa deve ler uma mensagem do usuário. Em seguida, deve traduzir 
# todas as letras e dígitos da mensagem para o código Morse, deixando um espaço
#  entre cada sequência de travessões e pontos. Seu programa deve ignorar quaisquer 
# caracteres que não estejam listados na tabela.

Codigo_Morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
'X': '-..-', 'Y': '-.--', 'Z': '--..',

'0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
'5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

texto = input('Digite a sua mensagem: ').upper() # upper()-> CAIXA ALTA
morse = ' '

for char in texto:
    for Key, Value in Codigo_Morse.items():
        if char == Key:
            morse += Value + ' '
print(morse)
print("tradução completa")
