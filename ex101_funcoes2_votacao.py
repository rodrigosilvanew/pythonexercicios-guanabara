from datetime import date
def voto():
    if idade < 16:
        return 'Negado'
    elif idade >= 16 and idade < 18 or idade >= 65:
        return 'Opcional'
    elif idade >= 18 and idade < 65:
        return 'Obrigatório'


ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
print(f'Com {idade} anos: O voto é {voto()}')


#VERSÃO DO GUANABARA:
'''def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


# Programa Principal:
nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))'''