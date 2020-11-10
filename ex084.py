totpes = 0
pessoas = []
lista = pessoas[:]
while True:
    pessoas.append(str(input('Digite o nome: ')))
    pessoas.append(float(input('Digite o peso: ')))
    totpes += 1
    opcao = str(input('Deseja continuar? [S/N]: ').strip().upper()[0])
    if opcao == 'N':
        break
print(f'{totpes} pessoas foram cadastradas.')
