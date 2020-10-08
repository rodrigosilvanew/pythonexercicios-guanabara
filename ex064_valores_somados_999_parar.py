n = 0
tot = 0
soma = 0
while n != 999:
    n = int(input('Digite um número inteiro, ou 999 para encerrar o programa: '))
    if n != 999:
        tot += 1
        soma += n
print('Você digitou {} números e a soma de todos eles é {}'.format(tot, soma))

#VERSÃO DO GUANABARA

'''núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))

print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))'''
