import random
A = input('Primeiro aluno: ')
B = input('Segundo aluno: ')
C = input('Terceiro aluno: ')
D = input('Quarto aluno: ')
lista = [A, B, C, D]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
