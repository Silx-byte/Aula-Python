print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
a = 0
b = 1
proximo = a + b
quantidade = int(input('Quantos termos você gostaria de ver ? '))
tentativa = 0
while tentativa != quantidade:
    print('{} → '.format(a), end='')
    a = b
    b = proximo
    proximo = a + b
    tentativa += 1
print('Fim')


# Resolução do Professor Guanabara
print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
n1 = int(input('Quantos termos você quer mostrar ? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} → {}'.format(t1, t2), end='')
cont = 3 # começou com 3 pois ja mostra o dois primeiros termos
while cont <= n1:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → Fim')
