'''def lines():
    frase = str(input('Digite o texto: '))
    print('~'* len(frase))
    print(frase)
    print('~'* len(frase))


lines()'''

#RESPOSTA DO GUANABARA
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


#Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')