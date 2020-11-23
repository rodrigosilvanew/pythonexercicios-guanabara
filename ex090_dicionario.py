'''aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input('Digite a média do aluno: '))
if aluno['media'] >= 7:
    aluno['situaçao'] = 'Aprovado'
else:
    aluno['situaçao'] = 'Reprovado'
for c in aluno.values():
    print(f'O nome do aluno é {aluno["nome"]}')
    print(f'A média do aluno é {aluno["media"]}')
    print(f'A situação do aluno é {aluno["situaçao"]}')
    break'''


#VERSÃO DO GUANABARA:

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')