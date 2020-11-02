lista = []
pares = []
impares = []
while True:
    n = lista.append(int(input('Digite um número: ')))
    o = str(input('Deseja Continuar? [S/N]: ')).upper()[0]
    if o not in 'SN':
        o = str(input('Deseja Continuar? [S/N]: ')).upper()[0]
    if o == 'N':
        break
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(f'Você digitou a seguinte lista: {lista}')
print(f'Os números pares são {pares}')
print(f'Os números ímpares são {impares}')

#VERSÃO DO GUANABARA:

'''num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-='*30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')'''
