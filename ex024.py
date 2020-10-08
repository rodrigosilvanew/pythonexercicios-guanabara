'''  VERSÃO PROBLEMÁTICA, MAS PARCIALMENTE FUNCIONAL
name = str(input('Digite o nome da cidade em que você mora: '))
name2 = name.split()
res = name2[0].find('Santo')
print(res)'''

#VERSÃO CORRETA:

name = str(input('Digite o nome da cidade em que você mora: ')).strip()
print(name[:5].upper() == 'SANTO')
