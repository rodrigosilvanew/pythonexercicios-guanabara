import random, emoji
from time import sleep  #sleep faz com que o computador demore alguns segundos
n = int(input('Adivinhe qual o número escolhido pelo computador: '))
lista = [0, 1, 2, 3, 4, 5]
#lista = randint(0, 5)  o randint sortearia um número inteiro de 0 a 5.
print('-=-' * 50)
num = random.choice(lista)
print('PROCESSANDO...')
sleep(3)  #3 segundos
if n == num:
    print(emoji.emojize('PARABÉNS, você acertou. Como adivinhou o número? Você lê mentes????  :stuck_out_tongue_closed_eyes: ', use_aliases=True))
else:
    print(emoji.emojize('Sinto muito, mas você errou. Precisas treinar tuas técnicas mentais. Fala com o Professor X, talvez ele possa te ajudar! :disappointed:', use_aliases=True))
print('-=-' * 50)
