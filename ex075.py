num = (int(input('Digite um número: '))), (int(input('Digite um número: '))), (int(input('Digite um número: '))), (int(input('Digite um número: ')))
if 9 in num:
    print(f'O número 9 apareceu {num.count(9)} vezes')
else:
    print(f'O número 9 não aparece em nenhuma posição')
if 3 in num and num.count(3) == 1:
    print(f'O número 3 apareceu somente na posição {num.index(3) + 1}')
elif 3 in num and num.count(3) > 1:
    print(f'O número 3 apareceu primeiramente na posição {num.index(3) + 1}')
else:
    print('O número 3 não aparece em nenhuma posição')
if num % 2 == 0:
    print(f'Os números pares que apareceram são {}')