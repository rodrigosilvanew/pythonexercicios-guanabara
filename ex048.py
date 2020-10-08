soma = 0   #acumulador
cont = 0   #contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c  #forma abreviada de soma = soma + c
        cont += 1   #forma abreviada de cont = cont + 1
print('A soma de todos os {} valores escolhidos é {}'.format(cont, soma))
