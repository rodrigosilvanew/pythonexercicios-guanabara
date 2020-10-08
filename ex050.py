s = 0
b = 0
for c in range(1, 7):
    n = int(input('Digite aqui o {}º número: '.format(c)))
    if n % 2 == 0:
        s += n
        b += 1
print('Você digitou {} números pares e a soma deles é {}'.format(b, s))
#por algum motivo, o contador não está funcionando corretamente, tentar novamente depois...