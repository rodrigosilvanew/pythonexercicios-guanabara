'''s0 = 0
s1 = 'M'
s2 = 'F'
while s0 != s1 and s0 != s2:
    s0 = str(input('Digite aqui seu sexo [M/F]: ')).upper().strip()
    if s0 != s1 and s0 != s2:
        print('Você digitou uma opção inválida. Tente novamente.')'''




#versão do Guanabara:

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
