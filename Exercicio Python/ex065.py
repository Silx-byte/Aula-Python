resposta = 'S'
cont = 0
valor = 0
media = 0
maior = 0
menor = 0
continuar = ""
while resposta in 'Ss':
    num = int(input('Digite um numero: '))
    valor += num
    cont += 1
    media = valor / cont
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Você deseja continuar ? ')).strip().upper()[0]
print('A soma entre os numeros digitados foi {}, quantidade de numeros digitados foi {} e a media foi {}'.format(valor, cont, media))
print('O maior numero foi {} e o menor foi {}'.format(maior, menor))

# Resolução do Professor Guanabara

resp = 'S'
soma = quant = média = maior = menor = 0 # Podemos fazer isso quando temos varias váriaveis que terão seu valor inicial em 0
while resp in 'Ss':
    núm = int(input('Digite um valor: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))