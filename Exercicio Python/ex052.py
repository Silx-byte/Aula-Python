'''n = int(input('Digite um numero: '))
div = 0
for c in range(1, n+1):
    if n % c == 0:
        div = div + 1
if div == 2:
    print('O número {} é um número PRIMO! '.format(n))
else:
    print('O número {} NÃO É um número PRIMO!'.format(n))'''


# Resolução do Professor Guanabara

num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1 # Podendo ser feito também - tot = tot + 1
    else:
        print('\033[31m', end= ' ')
    print('{}'.format(c), end=' ')
print('\nO numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('É um numero primo')
else:
    print('Ele não é um numero primo')

