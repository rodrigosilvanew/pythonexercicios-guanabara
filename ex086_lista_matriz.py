matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um número para a posição [{linha}, {coluna}]: '))
for linha in range(0, 3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print() #esse print vazio vai servir pra quebrar as colunas