print('*' * 37)
print(' '* 8,'RODRIGONEW BANK')
cinquenta = vinte = dez = um = 0
while True:
    valor = int(input('Digite o valor que deseja sacar: '))
    if valor % 50 == 0:
        cinquenta = valor / 50
    else:
        cinquenta = valor // 50
        tira50 = valor - (cinquenta * 50)
        if tira50 % 20 == 0:
            vinte = tira50 / 20
        else:
            vinte = tira50 // 20
            tira20 = tira50 - (vinte * 20)
            if tira20 % 10 == 0:
                dez = tira20 / 10
            else:
                dez = tira20 // 10
                tira10 = tira20 - (dez * 10)
                if tira10 % 1 == 0:
                    um = tira10 / 1
    break
print(f'''Total de {cinquenta:.0f} cédulas de R$50
Total de {vinte:.0f} cédulas de R$20
Total de {dez:.0f} cédulas de R$10
Total de {um:.0f} cédulas de R$1
''')
print('*' * 37)
print(' '*7 ,'OPERAÇÃO ENCERRADA')