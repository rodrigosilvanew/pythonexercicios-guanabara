'''import random
from time import sleep

tot = 1
c = random.randint(0, 10)

n = int(input('Digite aqui o número que você acha que o computador escolherá entre 0 e 10: '))
while n != c:
    if n != c:
        tot += 1
        n = int(input('Você errou, tente novamente: '))
    else:
        tot += 1
if tot == 1:
    print('Incrível!!! Você acertou de primeira!!!!!')
else:
    print('Você acertou, mas só conseguiu na {}ª tentativa'.format(tot))'''


#VERSÃO DO GUANABARA:

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
