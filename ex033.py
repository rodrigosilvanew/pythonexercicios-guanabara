num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
list = [num1, num2, num3]
print('O maior número é {}.'.format(max(list)))
print('O menor número é {}.'.format(min(list)))



'''   OUTRA FORMA DE FAZER

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
#verificando quem é menor:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando quem é o maior:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))
'''