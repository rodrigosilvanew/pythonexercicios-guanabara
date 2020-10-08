import math
num = int(input('Digite o ângulo: '))
S = math.sin(math.radians(num))
C = math.cos(math.radians(num))
T = math.tan(math.radians(num))
print('O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.'.format(S, C, T))
