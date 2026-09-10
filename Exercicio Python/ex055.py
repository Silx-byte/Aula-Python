maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input('Digite seu peso: '))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            peso = menor
print('O Maior peso foi {} e o MENOR peso foi {}!'.format(maior, menor))

    
