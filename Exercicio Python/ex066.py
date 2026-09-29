valor = int(input('Digite um valor: '))
soma = 0
digitados = 0

while not valor == 999:
    soma += valor
    digitados += 1
    valor = int(input('Digite outro valor:'))
    if valor == 999:
        print(f'{soma, digitados}')

# Resolucao do Professor Guanabara


soma = cont = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    soma += n
    cont += 1
    
print(f'Você digitou {cont} numeros, a soma entre eles é {soma}')