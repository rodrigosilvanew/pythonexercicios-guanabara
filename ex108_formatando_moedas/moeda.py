def metade(n = 0):
    m = n / 2
    return m

def dobro(n = 0):
    m = n * 2
    return m

def aumento(n = 0, t = 0):
    aum = (n * t/100) + n
    return aum

def reduz(n = 0, t = 0):
    red = n - (n * t/100)
    return red

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')