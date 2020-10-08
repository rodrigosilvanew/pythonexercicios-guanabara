C = float(input('Informe a temperatura em ºC: '))
f = ((9*C)/5)+32
#ou f = ((9*C)/5)+32  ----- pela ordem de precedência, não precisaria dos parênteses
print('A temperatura de {}ºC corresponde a {}ºF!'.format(C, f))
