ordens = ('Blatodeos', 'Coleopteros', 'Dipteros', 'Fasmideos', 'Ftirapteros', 'Hemipteros', 'Himenopteros',
          'Isopteros', 'Lepidopteros', 'Odonatos', 'Ortopteros', 'Tisanuros')
for c in ordens:
    print(f'\na palavra {c} tem as vogais ', end='') #cada palavra em 'ordens' também é uma lista (uma lista de letras)
    for letra in c:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
