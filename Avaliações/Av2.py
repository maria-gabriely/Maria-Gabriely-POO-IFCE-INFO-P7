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
   # x = Codigo_Morse[char]
    for Key, Value in Codigo_Morse.items():
        if char == Key:
            morse += Value + ' '
print(morse)
print("tradução completa")