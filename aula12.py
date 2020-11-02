nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:                                                  #o else é opcional. Porém, não pode usar elif sem if! (elif = else + if)
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
