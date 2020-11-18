ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('*'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    escolha = int(input('Mostrar as notas do aluno número (999 encerra o programa): '))
    if escolha == 999:
        break
    if escolha <= len(ficha) -1:
        print(f'Notas de {ficha[escolha][0]} são {ficha[escolha][1]}')