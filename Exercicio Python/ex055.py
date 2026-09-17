'''maior = 0
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

    
# Utilizamos o IF C == 0 Para padronizarmos os valores tanto de maior quanto de menor
# Quando fazemos isso, podemos utilizar o ELSE para mostrar que caso tenha mais de 1 opção
# Ele consiga avaliar todos e fazer com que a gente consiga criar essa separação do maior para o menor.'''

# Resolucao do Professor Guanabara

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso da {} pessoa: '.format(c))) # Para que o .format funcione antes, ele precisa estar dentro dos (''.format), se não ele só formataria quando o codigo acabasse. Ficaria errado
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {} o menor peso foi {}'.format(maior, menor))