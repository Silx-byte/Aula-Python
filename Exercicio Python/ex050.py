'''soma = 0
for c in range(0 , 6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        soma = soma + n
print('A soma de todos os numeros pares e {}'.format(soma))'''


# Resolucao do Professor Guanabara

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} numero: '.format(c)))
    soma += num
    cont += 1
print('Voce informou {} números e a soma foi {}'.format(cont, soma))
