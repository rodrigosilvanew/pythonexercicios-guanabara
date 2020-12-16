def metade(n = 0, formatado=False):
    m = n / 2
    return m if not formatado else moeda(m)

def dobro(n = 0, formatado=False):
    m = n * 2
    return m if not formatado else moeda(m)

def aumento(n = 0, t = 0, formatado=False):
    aum = (n * t/100) + n
    return aum if formatado is False else moeda(aum)

def reduz(n = 0, t = 0, formatado=False):
    red = n - (n * t/100)
    return red if formatado is False else moeda(red)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')