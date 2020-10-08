print('==== LOJAS RODRIGONEW ====')
soma = totmil = menor = cont = 0
produto = ' '
while True:
    print('='*25)
    nome = str(input('Digite o nome do produto: ')).strip().upper()
    preco = float(input('Digite o preço do produto: '))
    while preco < 0:
        print('PREÇO INVÁLIDO, DIGITE UM PREÇO VÁLIDO!')
        preco = float(input('Digite o preço do produto: '))
    print('='*25)
    soma += preco
    cont += 1
    if cont == 1: # essa linha poderia ser: *if cont == 1 or preco < menor:* e apagaria a parte do if preco < menor:
        produto = nome
        menor = preco
    if cont > 1:
        if preco < menor:
            produto = nome
            menor = preco
    if preco > 1000:
        totmil += 1
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print('='*49)
print(f'O total a ser pago é {soma}.')
print(f'Tem-se {totmil} produtos que custam acima de 1000 reais.')
print(f'O produto mais barato é {produto} custando {menor}')
print('='*49)