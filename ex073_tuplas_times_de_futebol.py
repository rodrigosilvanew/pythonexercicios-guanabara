times = ('Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Santos', 'Fluminense', 'Fortaleza',
         'Palmeiras', 'Atlético-GO', 'Corinthians', 'Grêmio', 'Sport Recife', 'Bahia', 'Ceará-SC', 'Botafogo',
         'Vasco da Gama', 'Athletico-PR', 'Coritiba', 'Bragantino-SP', 'Goiás')
print('*'*33)
print(f'Os cinco primeiros colocados são: \n{times[0:5]}')
print('*'*33)
print(f'Os últimos quatro colocados são {times[-4:]}')
print('*'*33)
print(f'Times em ordem Alfabética: \n{sorted(times)}')
print('*'*33)
print(f'O Coritiba está na posição {times.index("Coritiba")}') #Temos que usar aspas duplas aqui nesse index, pois já estamos dentro de aspas simples, para que o Python entenda a interpolação. Também podemos usar o .format como mostrado abaixo
print('*'*33)
print('O Coritiba está na posição {}'.format(times.index('Coritiba')))
