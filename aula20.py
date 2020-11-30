#PARTE 01
def lin():
    print('-' * 30)


'''print('   CURSO EM VÍDEO   ')
print('-' * 30)
print('-' * 30)
print('   APRENDA PYTHON   ')
print('-' * 30)
print('-' * 30)
print('   GUSTAVO GUANABARA   ')
print('-' * 30)'''

'''lin()
print('   CURSO EM VÍDEO   ')
lin()
lin()
print('   APRENDA PYTHON   ')
lin()
lin()
print('   GUSTAVO GUANABARA   ')
lin()'''

#PARTE 02
'''def soma(a, b):
    s = a + b
    print(s)


#Programa Principal
soma(4, 5)
soma(8, 9)
soma(2, 1)'''



'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


#Programa Principal
soma(b=4, a=5)
soma(7, 2)'''

#Parte 03
'''def contador(* núm): #o * é usado como símal de desempacotamento e informa que não se sabe quantos parâmetros serão informados
    print(núm)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''


'''def contador(* núm): #o * é usado como símal de desempacotamento e informa que não se sabe quantos parâmetros serão informados
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''


'''def contador(* núm): #o * é usado como símal de desempacotamento e informa que não se sabe quantos parâmetros serão informados
    tan = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tan} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''



#Parte 04
'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)'''


'''def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)'''
