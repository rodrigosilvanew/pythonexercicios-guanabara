numeros = [[], []]
for c in range(0, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares foram {numeros[0]}')
print(f'Os números ímpares foram {numeros[1]}')
