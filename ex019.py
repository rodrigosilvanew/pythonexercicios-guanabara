import random
A = input('Digite o nome do primeiro aluno: ')
B = input('Digite o nome do segundo aluno: ')
C = input('Digite o nome do terceiro aluno: ')
D = input('Digite o nome do quarto aluno: ')
lista = [A, B, C, D]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))
