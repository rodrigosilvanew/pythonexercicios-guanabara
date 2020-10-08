print('Olá, vamos calcular o aumento do seu salário. Ânimo!!!')
sal = float(input('Digite aqui seu atual salário: '))
if sal > 1250:
    print('Seu novo salário é {}.'.format(sal * 0.1 + sal))
else:
    print('Seu novo salário é {}.'.format(sal * 0.15 + sal))
