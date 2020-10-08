'''
print('='*10 , 'Sistema de compras das lojas New' , '='*10)

preco = float(input('Digite o preço normal do produto: '))

print('Por favor, informe o método de pagamento desejado: ')
print('Para pagar à vista com dinheiro ou cheque e receber um desconto de 10%, digite 1')
print('Para pagar à vista com no cartão com desconto de 5%, digite 2: ')
print('Para pagar em até 2x no cartão o preço normal do produto, digite 3')
print('Para pagar em 3x ou mais no cartão com juros de 20%, digite 4')

opcao = int(input('Digite aqui a opção desejada: '))
dinche = preco - preco *(10 / 100)
cartao = preco - preco * (5 / 100)
cartao2x = preco
cartao3xm = preco + preco * (20 / 100)



if opcao == 1:
    print('O valor a ser pago é {}'.format(dinche))
elif opcao == 2:
    print('O valor a ser pago é {}'.format(cartao))
elif opcao == 3:
    print('O valor a ser pago é {}'.format(cartao2x))
elif opcao == 4:
    print('O valor a ser pago é {}'.format(cartao3xm))

'''

#forma mais organizada do Guanabara:

print('{:=^40}'.format('LOJAS RODRIGONEW'))   #o ^ significa centralizado e o 40 indica que será centralizado em 40 espaços
preço = float(input('Preço das Compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço - 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas Parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} sem juros'.format(totalparc, parcela))
    print('Sua compra será parcelada em 2x de {:.2f}'.format(parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
