#BLOCO 1
'''num = [2, 5, 9, 1]
num[2] = 3 #listas são mutáveis
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o 5')
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''

#BLOCO 2

'''valores = [] #também dá pra criar uma lista vazia com valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
#print(valores)
#for v in valores:
#    print(f'{v}...', end='')

for c, v in enumerate(valores): #o enumerate dá tanto a posição como o dado
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''


'''valores = [] #também dá pra criar uma lista vazia com valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''

#BLOCO 3

a = [2, 3, 4, 7]
#b = a #ao igualar duas listas, o Python cria uma ligação entre elas. Portanto, se alterar um valor de uma, alterará o mesmo valor na outra
b = a[:] #assim, criamos uma cópia de todos os elementos de a para o b e a ligação não existe mais, permitindo que as listas sejam alteradas individualmente
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')