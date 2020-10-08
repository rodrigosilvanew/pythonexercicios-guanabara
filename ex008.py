n = float(input('Digite um valor em m: '))
c = n * 100
m = n * 1000
dam = n / 10
hm = n / 100
km = n / 1000
print('Você digitou {} m. \n Em centímetros é {:.0f}. \n Em milímetros é {:.0f}.'.format(n, c, m))
print(' Em dam {}m \n Em hm {}m \n em km {}m.'.format(dam, hm, km))
