print('-=-'*24)
print('Está é a pré calculadora de RodrigoNew. Sinta-se livere para utilizá-la.')
print('-=-'*24)
maior = 0
num1 = float(input('Digite aqui o primeiro número: '))
num2 = float(input('Digite aqui o segundo número: '))
print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
operacao = int(input('Digite aqui o número correspondente à operação que você deseja realizar: '))
while operacao != 5:
    if operacao == 1:
        print(num1 + num2)
        operacao = int(input('Deseja realizar uma nova operação? '))
    elif operacao == 2:
        print(num1 * num2)
        operacao = int(input('Deseja realizar uma nova operação? '))
    if operacao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(maior)
        operacao = int(input('Deseja realizar uma nova operação? '))
    if operacao == 4:
        num1 = int(input('Digite aqui seu novo primeiro valor: '))
        num2 = int(input('Digite aqui seu novo segundo valor: '))
        operacao = int(input('Qual operação você deseja realizar agora? '))