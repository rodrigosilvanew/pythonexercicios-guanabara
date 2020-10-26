print(f'{"LISTA DE JOGOS DE PS4:":^38}') #O ^ serve para centralizar
jogos = ('God of War', 80, 'Red Dead Redemption 2', 250, 'Dying Light', 150, 'Horizon Zera Dawn', 80,
         'The Last of Us: Part 2', 280, "Marvel's Spider-Man", 130, 'Death Stranding', 146.50,
         'Bloodborne', 80, 'Sekiro: Shadows Die Twice', 230)
for game in range(0, len(jogos)):
    if game % 2 == 0:
        print(f'{jogos[game]:.<30}', end='') #O < serve para alinhar à esquerda. 30 é a quantidade de "espaços"
    else:
        print(f'R${jogos[game]:>7.2f}') #O > serve para alinhar à direita