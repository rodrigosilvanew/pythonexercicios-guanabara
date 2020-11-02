#lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita') #tuplas também podem ser escritas sem parênteses
#tuplas são imutáveis
#lanche[1] = 'Refrigerante'
#print(lanche)

#for cont in range(0, len(lanche)):
#    print(f'Eu vou comer {lanche[cont]}')

#for comida in lanche:
#    print(f'Eu vou comer {comida}')

#for cont in range(0, len(lanche)):
#    print(f'Eu vou comer {lanche[cont]} na posiçao {cont}')

#for pos, comida in enumerate(lanche): #o enumerate dá tanto a posição como o dado
#    print(f'Eu vou comer {comida} na posição {pos}')

#print(sorted(lanche)) #sorted mostra a tupla em ordem, mas não altera de verdade

'''a = (2, 5, 4) #o símbolo + concatena tuplas
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(c)
print(d)
print(len(c))
print(c.count(5)) #mostra quantas vezes o 5 aparece em c
print(c.index(8)) #mostra em qual posição está o 8'''

pessoa = ('Gustavo', 39, 'M', 99.88) #no python, as tuplas aceitam dados diferentes
#del(pessoa) #o comando del() apaga qualquer coisa
print(pessoa)
