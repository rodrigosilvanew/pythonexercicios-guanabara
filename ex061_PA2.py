prim = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão da PA: '))
termo = prim
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += raz
    cont += 1

