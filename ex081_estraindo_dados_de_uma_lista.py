lista = []
while True:
    n = lista.append(int(input('Digite um número: ')))
    o = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    if o not in 'SN':
        o = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    if o == 'N':
        break
print(f'A lista é {lista}')
print(f'Você digitou {len(lista)} números')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O 5 está presente na lista')
else:
    print('O 5 não está presente na lista')
    