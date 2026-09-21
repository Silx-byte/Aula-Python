'''contador = int(input('Digite um numero: '))
resultado = 1
while not contador == 0:
    resultado = resultado * contador
    if contador > 1:
        print(contador, end = ' x ')
    else:
        print(contador, end='')
    contador -= 1
print(' = {}'.format(resultado))'''

'''contador = int(input('Digite um numero: '))
resultado = 1
for c in range(0, contador):
    resultado *= contador
    if contador > 1:
        print(contador)
    else:
        print(contador)
    contador -= 1
print(resultado)'''

# Resolução do Professor Guanabara

n = int(input('Digite um numero para calcular seu Fatorial: '))
c = n
f = 1 # O fator NULO de multiplicação é 1 pois qualquer multiplicação por 0 da 0
print('Calculando {}! = '.format(n), end='')
while c > 0: # Em portugol - Enquanto c for maior que 0 ele repete.
    print('{}'.format(c), end= '' )
    print(' x ' if c > 1 else ' = ', end= '') # Colocamos o if dentro do print para ele mostrar X enquanto o C for maior do que 1. Quando ele for menor, mostrar o =. Mostrando a possibilidade de usar IF dentro de PRINT
    f *= c
    c -= 1
print('{}'.format(f))
