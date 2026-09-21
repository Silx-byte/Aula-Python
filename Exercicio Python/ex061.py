n1 = int(input('Digite um valor: '))
razão = int(input('Digite a Razão: '))
cont = 1
termo = n1
while cont <=10:
    termo += razão
    print('{} → '.format(termo), end='')
    cont += 1
print('FIM')