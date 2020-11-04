expressão = str(input('Digite uma expressão matemática: '))
lista = []
for c in expressão:
    if c == '(':
        lista.append('(')
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('A expressão é válida.')
else:
    print('A expressão não é válida.')