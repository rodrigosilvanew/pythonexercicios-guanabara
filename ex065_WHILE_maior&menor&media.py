resposta = 'SIM'
negativo = 'NÃONAO'
cont = 0
soma = 0
maior = 0
menor = 0
while resposta not in negativo:
    num = int(input('Digite um número inteiro: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = num
        menor = num
    if cont > 1:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Deseja continuar? ')).strip().upper()
print('A média é {:.1f}, o maior valor é {} e o menor valor é {}'.format(soma / cont, maior, menor))


#VERSÃO DO GUANABARA:

'''resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]  #o [0] serve para só considerar a primeira letra
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))'''
