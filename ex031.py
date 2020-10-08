dist = float(input('Qual a distância, em quilômetros, percorrida na viagem? '))
if dist <= 200:
    print('Sua passagem custa {} reais.'.format(dist * 0.5))
else:
    print('Sua passagem custa {} reais.'.format(dist * 0.45))
print('Boa Viagem!')

'''
De forma simplificada:
preço = dist * 0.5 if dist <= 200 else dist * 0.45
'''