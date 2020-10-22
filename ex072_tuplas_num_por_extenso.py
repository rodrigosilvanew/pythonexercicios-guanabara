extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',\
          'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',\
          'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
for num in range(0, len(extenso)):
    num = int(input('Digite um número de 0 a 20: '))
    while num < 0 or num > 20:
        num = int(input('Número inválido! Digite um número entre 0 e 20: '))
    print(f'Você digitou {extenso[num]}')
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    else:
        if opcao == 'N':
            print('PROGRAMA ENCERRADO')
            break

#VERSÃO DO GUANABARA

'''cont = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',\
          'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',\
          'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[núm]}')'''
