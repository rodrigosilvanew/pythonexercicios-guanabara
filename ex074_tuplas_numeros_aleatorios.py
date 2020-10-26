from random import randint
numeros = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print(f'Os números sorteados são ', end='')
for c in numeros: #esse for foi inserido para que os números não aparecessem entre ()
    print(f'{c} ', end='')
print(f'\nO maior valor é {max(numeros)}')
print(f'O menor valor é {min(numeros)}')