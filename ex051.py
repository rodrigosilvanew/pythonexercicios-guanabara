primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end='→ ')   #pra colocar a setinha pra direita ALT + 26 ( →)
print('ACABOU!')
