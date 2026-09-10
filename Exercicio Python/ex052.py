n = int(input('Digite um numero: '))
div = 0
for c in range(1, n+1):
    if n % c == 0:
        div = div + 1
if div == 2:
    print('O número {} é um número PRIMO! '.format(n))
else:
    print('O número {} NÃO É um número PRIMO!'.format(n))

    