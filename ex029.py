vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    print('Você excedeu a velocidade limite. Sua multa é de {} reais.'.format((vel - 80) * 7))
    print('Mais cuidado na próxima vez!')
'''else:
    print('Nenhuma infração registrada.')
    print('Dirija com segurança!')'''
print('Dirija com segurança e tenha um ótimo dia!')
