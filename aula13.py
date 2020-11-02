'''for c in range(6, 0, -1):   # ele ignora o último número   / se colocar (x, y, -1) ele vai contando de trás pra frente
    print(c)
print('FIM')
'''


'''
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
'''

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}.'.format(s))
