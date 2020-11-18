matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maior = somacoluna = 0
for linha in range(0, 3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um número para a posição [{linha}, {coluna}]: '))
for linha in range(0, 3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
    print() #esse print vazio vai servir pra quebrar as colunas
print('*'*42)
print(f'A soma dos números pares é {somapar}')
for linha in range(0, 3):
    somacoluna += matriz[linha][2]
print(f'A soma dos números da terceira coluna é {somacoluna}')
for coluna in range(0, 3):
    if coluna == 0 or matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior número na linha 2 é {maior}')
