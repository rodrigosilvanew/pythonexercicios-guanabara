'''from datetime import date
cadastro = dict()
cadastro['Nome'] = str(input('Digite o nome: '))
nascimento = int(input('Digite seu ano de nascimento: '))
cadastro['Idade'] = date.today().year - nascimento
cadastro['CTPS'] = int(input('Digite o número da CTPS (Digite 0 se não tiver carteira): '))
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Digite o ano de contratação: '))
    cadastro['Salário'] = float(input('Digite o salário: '))
    if (date.today().year - cadastro['Contratação']) < 35:
        cadastro['Aposentadoria'] = 35 - ((date.today().year - cadastro['Contratação'])) + cadastro['Idade']
    else:
        cadastro['Aposentadoria'] = 'Já pode se aposentar'
    print('*' * 30)
    for k, v in cadastro.items():
        print(f'{k} tem o valor {v}')
else:
    for k, v in cadastro.items():
        print(f'{k} tem o valor {v}')'''


#VERSÃO DO GUANABARA

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
    print('-='*30)
for k, v in dados.items():
    print(f'   - {k} tem o valor {v}')
