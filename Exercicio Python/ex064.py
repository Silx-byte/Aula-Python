valor = int(input('Digite um valor [Digite 999 para parar]:  '))
soma = 0
numeros = 0
while not valor == 999:
    soma += valor
    numeros += 1
    valor = int(input('Digite outro valor [Digite 999 para parar]: '))
print('Você digitou {}, a soma entre eles é {}'.format(numeros, soma))


# Resolucao do Professor Guanabara

num = cont = soma = 0
num = int(input('Digite um valor [Digite 999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um valor [Digite 999 para parar]: '))
print('Você digitou {}, e a soma entre eles é {}'.format(cont, soma))