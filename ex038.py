num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print('O primeiro valor é maior.')
elif num2 > num1:
    print('O segundo valor é maior.')
else:
    print('Os dois valores são iguais.')

'''elif num1 == num2:
    print('Não existe valor maior, os dois números são iguais.')'''  #poderia ter feito com elif, mas com else fica mais curto