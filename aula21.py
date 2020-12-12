#**INTERACTIVE HELP**
#help() - adquirir informações sobre funções, métodos e etc
#help(print) - também pode colocar a função ou método dentro dos parênteses
#print(input.__doc__) informações sobre o comando


#**DOCSTRING** - é uma string de documentação
#A função abaixo será usada como exemplo:
'''def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='.. ')
        c += p
    print('FIM')

help(contador)'''

#**PARÂMETROS OPCIONAIS**
'''def somar(a=0, b=0, c=0):
    """
    Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Gustavo Guanabara do CursoemVideo
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(2, 1)'''


#**ESCOPO DE VARIÁVEIS**
'''def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa Principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}')'''
#ocorrerá um erro, pois x é uma variável de escopo local. Já n é uma variável de escopo global.

'''def funcao():
    global n1 #o comando global transforma a variável local em global
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')'''



#**RETORNANDO VALORES**

'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')'''



#**EXEMPLOS PRÁTICOS**

'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')'''


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')