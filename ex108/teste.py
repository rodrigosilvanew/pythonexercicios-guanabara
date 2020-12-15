import moeda

p = float(input('Digite o Preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumento(p, 10))}')
print(f'Reduzindo 13%, temos {moeda.reduz(p, 13)}')