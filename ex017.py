from math import pow, sqrt, hypot
CO = float(input('Digite o valor do Cateto Oposto: '))
CA = float(input('Digite o valor do Cateto Adjacente: '))
#HI = sqrt(pow(CO, 2) + pow(CA, 2))
#print('O valor da hipotenusa é igual a {:.2f}.'.format(HI))
HI = hypot(CA, CO)
print('O valor da hipotenusa é {:.2f}.'.format(HI))
