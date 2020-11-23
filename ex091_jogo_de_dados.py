from random import randint
from time import sleep
from operator import itemgetter #ittemgetter() necessário para ordenar o dicionário
print('Valores sorteados:')
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
ranking = list()
for k, v in jogadores.items():
    sleep(1)
    print(f'{k} tirou {v} no dado.')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('Resultado dos jogadores:')
for i, v in enumerate(ranking):
    sleep(1)
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}')