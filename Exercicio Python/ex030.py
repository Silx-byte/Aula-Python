n = int(input('Digite um numero: '))
if n % 2 == 0:
    print('O seu numero e par')
else:
    print('Seu numero e impar')


# Resolucao do Professor Guanabara

numero = int(input('Me diga um numero qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O numero {} e PAR'.format(numero))
else:
    print('O numero {} e IMPAR'.format(numero))
    