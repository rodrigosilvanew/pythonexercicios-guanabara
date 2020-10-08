import random
cont = 0
while True:
    maquina = random.randint(0, 10)
    num = int(input('Digite um número: '))
    soma = num + maquina
    opcao = str(input('Par ou Impar? [P/I]:')).strip().upper()
    if soma % 2 == 0 and opcao == 'P' or soma % 2 != 0 and opcao == 'I':
        print(f'Você jogou {num} e a máquina jogou {maquina}. A soma é {soma}. Parabéns, você VENCEU!!!')
        cont += 1
    else:
        print(f'Você jogou {num} e a máquina jogou {maquina}. A soma é {soma}. VOCÊ PERDEU!!!')
        if cont == 1:
            print(f'Você venceu {cont} vez.')
        else:
            print(f'Você venceu {cont} vezes.')
        break

#VERSÃO DO GUANABARA

'''from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')'''
