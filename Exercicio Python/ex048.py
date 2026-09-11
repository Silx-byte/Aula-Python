'''soma = 0
for c in range(1, 501):
    impar = c % 2 == 1
    div = c % 3 == 0
    if div and impar:
        soma = soma + c
print('A soma de todos os numeros Impares e Divisiveis por 3 e: {}'.format(soma))'''


# Resolucao do Professor Guanabara

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos {} valores solicitados resulta em {}'.format(cont, soma))