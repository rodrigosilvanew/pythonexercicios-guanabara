'''
print("Vamos descobrir se temos um triângulo e qual tipo de triângulo tempos:")
l1 = float(input('Digite aqui o valor do primeiro lado do triângulo: '))
l2 = float(input('Digite aqui o valor do segundo lado do triângulo: '))
l3 = float(input('Digite aqui o valor do terceiro lado do triângulo: '))

if (l1 + l2 > l3) and (l2 + l3 > l1) and (l1 + l3 > l2) and l1 == l2 == l3:
    print('Temos um triângulo EQUILÁTERO')
elif (l1 + l2 > l3) and (l2 + l3 > l1) and (l1 + l3 > l2) and (l1 == l2 != l3) or (l2 == l3 != l1) or (l1 == l3 != l2):
    print('Temos um triângulo ISÓSCELES')
elif (l1 + l2 > l3) and (l2 + l3 > l1) and (l1 + l3 > l2) and (l1 != l2 != l3 != l1):
    print('Temos um triângulo ESCALENO')
'''
#FORMA MELHOR:

r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')   #end='' faz com que no fim dá linha não seja aplicado um "enter"
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1: #importante repetir o r1 no final para garantir que r3 também é diferente de r1 e não só de r2
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')