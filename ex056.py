'''velho = 0
novo = 0
soma = 0
totm = 0
idadeh = 0
for c in range(1, 5):
    nome = str(input('Digite aqui o nome da {}ª pessoa: '.format(c)))
    idade = int(input('Digite aqui a idade da {}ª pessoa: '.format(c)))
    genero = str(input('Sexo [M/F]: '.format(c))).strip()
    soma += idade
    media = soma / 4
    if idade < 20 and genero == 'mulher':
        totm += 1
    if c == 1:
        velho = c
        novo = c
    else:
        if idade > velho:
            velho = idade
        if idade < novo:
            novo = idade
    if c == 1 and genero in 'Mm':
        idadeh = idade


print('-=-'*20)
print('A média de idade do grupo é {}'.format(media))
print('Têm {} mulheres com menos de 20 anos de idade'.format(totm))'''

#SOLUÇÃO GUANABARA:

somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range (1,5):
    print('-----{}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > 20:
        totmulher20 += 1

médiaidade = somaidade / 4
print('A média de idade do grupo é de {}'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
