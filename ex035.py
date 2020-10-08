print('Será que conseguiremos formar um triângulo com os lados fornecidos por você?')
l1 = float(input('Digite aqui o valor do primeiro lado: '))
l2 = float(input('Digite aqui o valor do segundo lado: '))
l3 = float(input('Digite aqui o valor do terceiro lado: '))
if (l1 + l2 > l3) and ((l2 + l3 > l1)) and (l1 + l3 > l2):
    print('É possível formar um triângulo com os lados fornecidos.')
else:
    print('Não é possível formar um triângulo com os lados fornecidos!')

#obs: a soma de dois lados tem que ser sempre maior que o terceiro lado para que se possa formar um triângulo