jogador = {}
partidas = []
jogador['Nome'] = str(input('Digite o nome: '))
tot = int(input(f'Quantidade de partidas do {jogador["Nome"]}: '))
for c in range(0, tot):
    partidas.append(int(input(f'Gols na partida {c}? ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas) #sum() soma os valores dentro da lista
print('*'*70)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('*'*70)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas')
for a, b in enumerate(jogador['Gols']):
    print(f'== Na partida {a}, fez {b} gols ==')
print(f'Total de {jogador["Total"]} gols')