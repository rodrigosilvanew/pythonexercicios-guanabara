nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print('VOCÊ ESTÁ REPROVADO!!!!!!')
elif 5.0 < media < 6.9:
    print('Você está em RECUPERAÇÃO. Comece a estudar!')
elif media >= 7.0:
    print('Parabéns, você foi aprovado. Não fez mais do que sua obrigação.')
