import calendar
from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano

print('Bem vindo ao serviço militar brasileiro!')
if idade < 18:
    print('Você ainda não tem idade para o alistamento.')
    print('Faltam {} anos para seu alistamento.'.format(18 - idade))
elif idade == 18:
    print('Chegou seu momento de se alistar. Por favor, compareça à junta militar da sua cidade.')
elif idade > 18:
    print('Você já deveria ter se alistado. Por favor, compareça o mais rápido possível à junta militar da sua cidade.')
    print('Você está {} anos atrasado'.format(idade - 18))

print('SERVIÇO MILITAR BRASILEIRO. VOCÊ NÃO TEM ESCOLHA, É OBRIGATÓRIO')
