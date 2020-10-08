soma = cont = 0
while True:
    n = int(input('Digite um número (999 encerra o programa): '))
    if n == 999:
        break #break antes de soma e cont fará com que 999 não seja contabilizado
    soma += n
    cont += 1
print(f'Você digitou {cont} números e a soma deles é {soma}')
