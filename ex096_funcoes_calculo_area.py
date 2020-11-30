def area(a, b):
    p = a * b
    print(f'A área de um terreno {larg}x{comp} é de {p}m²')


print('Controle de Terrenos')
print('-'*20)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)