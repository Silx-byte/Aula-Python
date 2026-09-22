n1 = int(input('Digite um valor: '))
razão = int(input('Digite a razão: '))
termo = n1
cont = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <=total :
        print('{}'.format(termo), end='→')
        termo += razão
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais você gostaria de ver ?'))
print('A quantidade de termos mostrado foi {} termos'.format(total))