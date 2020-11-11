maior = menor = 0
pessoas = []
lista = []
while True:
    lista.append(str(input('Digite o nome: ')))
    lista.append(float(input('Digite o peso: ')))
    if len(pessoas) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    pessoas.append(lista[:])
    lista.clear()
    opcao = str(input('Deseja continuar? [S/N]: ').strip().upper()[0])
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]: ').strip().upper()[0])
    if opcao == 'N':
        break
print(f'O total de pessoas foi {len(pessoas)}') #usar o len da lista ao invés de criar um contador
print(f'O maior peso foi {maior}. As pessoas com esse peso são ', end=' ')
for ma in pessoas:
    if ma[1] == maior:
        print(f'[{ma[0]}]', end=' ')
print(f'\nO menor peso foi {menor}. As pessoas com esse peso são ', end=' ')
for me in pessoas:
    if me[1] == menor:
        print(f'[{me[0]}]', end=' ')