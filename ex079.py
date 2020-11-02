lista = []
while True:
    num = lista.append(int(input('Digite um número: ')))
    opcao = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    if opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    if opcao == 'N':
        break
    if num in lista:
        lista.pop()
        print('O número já está na lista, digite outro!')
print(lista)