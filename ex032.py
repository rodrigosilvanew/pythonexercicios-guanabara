import calendar
from datetime import date
#calendar é um módulo que fornece funções relacionadas ao calendário
ano = int(input('Digite o ano e descubra se ele é bissexto. Digite 0 para analisar o ano atual: '))
ano2 = calendar.isleap(ano)
if ano == 0:
    ano = date.today().year
if ano2 == True:
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é ano bissexto!')

'''

#OUTRO JEITO DE FAZER O CÓDIGO:

from datetime import date
ano = int(input('Digite o ano e descubra se ele é bissexto. Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é um ano bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
'''