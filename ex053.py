frase = str(input('Digite uma frase, desconsiderando acentos: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
#inverso = junto[::-1]
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')