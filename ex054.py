from datetime import date
atual = date.today().year
tot = 0
for c in range(1, 8):
    ano = int(input('Digite aqui o {}º ano de nascimento: '.format(c)))
    if (atual - ano) >= 21:
        tot += 1
print('{} pessoas atingiram a maioridade e {} ainda não atingiram'.format(tot, c - tot))
