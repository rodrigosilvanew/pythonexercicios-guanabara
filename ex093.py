jogador = {}
jogador2 = []
jogador['Nome'] = str(input('Digite o nome: '))
jogador['Partidas'] = int(input('Quantas partidas ele jogou? '))
quantgols = []
quantgols.append(int(input('Quantos gols na partida 0? ')))
quantgols.append(int(input('Quantos gols na partida 1? ')))
quantgols.append(int(input('Quantos gols na partida 2? ')))
quantgols.append(int(input('Quantos gols na partida 3? ')))
quantgols.append(int(input('Quantos gols na partida 4? ')))
jogador['Gols'] = quantgols
print('*'*50)
jogador2.append(jogador.copy())

for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')

print(jogador2)