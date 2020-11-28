times = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Digite o nome: '))
    tot = int(input(f'Quantidade de partidas do {jogador["Nome"]}: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Gols na partida {c+1}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas) #sum() soma os valores dentro da lista
    times.append(jogador.copy()) #não pode fazer fatiamento de dicionários, tem que usar o método copy
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        else:
            print('RESPONDA APENAS SIM OU NÃO!')
    if resp == 'N':
            break
print('*'*70)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('*'*70)
for k, v in enumerate(times):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('*'*70)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para]: '))
    if busca == 999:
        break
    if busca >= len(times):
        print('ERRO! Não existe jogador com esse código.')
    else:
       print(f'LEVANTAMENTO DO JOGADOR {times[busca]["Nome"]}: ')
       for i, g in enumerate(times[busca]['Gols']):
           print(f'No jogo {i+1} fez {g} gols')
    print('*'*40)
