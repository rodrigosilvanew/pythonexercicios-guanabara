name = str(input('Digite seu nome completo: ')).strip()
print('Descrevendo seu nome: ')
print('Seu nome em letras maiúsculas: ', name.upper())
print('Seu nome em letras minúsculas: ', name.lower())
print('Seu nome tem {} letras.'.format(len(name.replace(' ', ''))))
#print('Seu nome tem {} letras.'.format(len(name) - name.count(' ')))
name2 = name.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(name2[0], len(name2[0])))
#print('Seu primeiro nome é {} e ele tem {} letras'.format(name, nome.find(' ')))
