#PARTE 01

#pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#print(pessoas['nome'])
#print(pessoas['sexo'])
#print(pessoas['idade'])
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #É necessário usar aspas duplas para que não haja conflito com as aspas simples da string
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
'''for k in pessoas.keys():
    print(k)'''
'''for k in pessoas.values():
    print(k)'''
#del pessoas['sexo']
#pessoas['nome'] = 'Leandro'
'''for k, v in pessoas.items():
    print(f'{k} = {v}')'''


#PARTE 02

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])'''

#PARTE 03

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #.copy() é um método para copiar os elementos (não é fatiamento)
#print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')