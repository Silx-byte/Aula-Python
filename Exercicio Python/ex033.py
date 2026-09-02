# Minha resolucao
'''n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite o terceiro numero: '))
maior = n1
menor = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print('O maior numero foi {} e o menor {}'.format(maior, menor))'''

# Resolucao do Professor Guanabara

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem e menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem e o maior
maior = a
if b > a  and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitaddo foi {}'.format(maior))
