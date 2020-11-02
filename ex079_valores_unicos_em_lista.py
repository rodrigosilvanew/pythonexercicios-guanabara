lista = []
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
    else:
        print('O número digitado já está na lista, digite outro número!')
    opcao = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    if opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    if opcao == 'N':
        break
print(sorted(lista))