print('*' * 30)
print('SISTEMA DE CADASTRO DE PESSOAS')
sexo = ' '
idadepessoas = conthomem = contmulheres = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite aqui seu sexo [M/F/O]: ')).strip().upper()[0]
    while sexo not in 'MFO':
        sexo = str(input('Digite aqui se sexo [M/F/O]: ')).strip().upper()[0]
    if idade > 18:
        idadepessoas += 1
    if sexo == 'M':
        conthomem += 1
    if idade < 20 and sexo == 'F':
        contmulheres += 1
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if continuar == 'N':
            break
print('*' * 98)
print(f'Temos {idadepessoas} pessoas com mais de 18 anos, {conthomem} pessoas do sexo masculino e {contmulheres} mulheres com menos de 20 anos.')
print('SISTEMA ENCERRADO')
print('*' * 98)