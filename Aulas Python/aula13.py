#Para o Python contrar para tras, precisamso informar como ele faria isso, nesse caso, ele diminuiria -1.
'''for c in range(6, 0, -1 ):
    print(c)
print('Fim')'''

# Podendo ser utilizado tambem da seguinte forma \/ Assim ele vai contar de 2 em 2.
'''for c in range(0, 7, 2):
    print(c)
print('Fim')'''

# Podendo ser feito tambem \/ Aonde o numero que colocarmos, o for vai comecar em 0 e vai adicionando +1 ate chegar no numero respectivo.
'''n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)
print('Fim')'''

# Pode ser feito tambem. Um programa que le o inicio, o fim e a quantidade de numeros que voce gostaria de pular.
'''i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')'''

# Podemos pedir para o programa fazer um somatorio de varios numeros tambem
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatorio de todos os valores foi{}'.format(s))