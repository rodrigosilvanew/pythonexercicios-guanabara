from datetime import date

ano = int(input('Digite aqui o seu ano de nascimento: '))
idade = date.today().year - ano

print('='*8 , 'Serviço de categorização da Confederação Nacional de Natação:' , '='*8)
if idade <= 9:
    print('Você pertence à categoria MIRIM')
elif 10 <= idade <= 14:
    print('Você pertence à categoria INFANTIL')
elif 15 <= idade <= 19:
    print('Você pertence à categoria JUNIOR')
elif idade == 20:
    print('Você pertence à categoria SÊNIOR')
elif idade > 20:
    print('Você pertence à categoria MASTER')
