'''
import random

print('*'*10, 'Vamos jogar Jokenpô. Tente vencer a máquina!', '*'*10)

pedra = str('pedra').upper().strip()
papel = str('papel').upper().strip()
tesoura = str('tesoura').upper().strip()
lista = [pedra, papel, tesoura]
maquina = random.choice(lista)
pessoa = str(input('Digite aqui se você escolhe Pedra, Papel ou Tesoura: ')).upper().strip()

if pessoa == maquina:
    print('Você escolheu {} e a máquina escolheu {}. Sem vencedores nessa rodada.'.format(pessoa, maquina))
elif pessoa == pedra and maquina == papel:
    print('Você escolheu {} e a máquina escolheu {}. Você perdeu!'.format(pessoa, maquina))
elif pessoa == pedra and maquina == tesoura:
    print('Você escolheu {} e a máquina escolheu {}. Você venceu. Parabéns!!!'.format(pessoa, maquina))
elif pessoa == papel and maquina == pedra:
    print('Você escolheu {} e a máquina escolheu {}. Você venceu. Parabéns!!!'.format(pessoa, maquina))
elif pessoa == papel and maquina == tesoura:
    print('Você escolheu {} e a máquina escolheu {}. Você perdeu!'.format(pessoa, maquina))
elif pessoa == tesoura and maquina == pedra:
    print('Você escolheu {} e a máquina escolheu {}. Você perdeu!'.format(pessoa, maquina))
elif pessoa == tesoura and maquina == papel:
    print('Você escolheu {} e a máquina escolheu {}. Você venceu. Parabéns!!!'.format(pessoa, maquina))
'''

#VERSÃO INFINITAMENTE MELHOR FEITA PELO GUANABARA:

from random import randint
from time import sleep       # permite usar o sleep(x) que cria um delay. O x é o tempo em segundos.
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)  #sorteia um número inteiro de x até y sendo randint(x, y)
print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=-' * 11)
if computador == 0:    # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:    # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:    #computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')