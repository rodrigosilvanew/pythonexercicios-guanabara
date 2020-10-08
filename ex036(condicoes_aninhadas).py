print('='*10, 'Sistema de empréstimos do banco amigo', '='*10)
casa = float(input('Informe o valor da casa desejada: '))
salario = float(input('Informe o valor do salário do solicitante: '))
anos = int(input('Informe em quantos anos o cliente pretende pagar: '))
parcelas = anos * 12
if (casa / parcelas) > (30 / 100) * salario:
    print('A solicitação de empréstimo foi recusada.')
else:
    print('A solicitação de empréstimo foi aceita.')
print('A prestação da sua casa será de : R${}.'.format(casa / parcelas), end='')  #end='' faz a linha abaixo subir e se unir ao final da de cima
print(' Análise finalizada.')
print('='*10, 'Sistema de empréstimos do banco amigo', '='*10)
