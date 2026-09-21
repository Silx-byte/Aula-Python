'''for c in range(1, 10):
    print(c)
print('FIM')'''

'''c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')'''

n = 1
par = impar = 0 # Quando ambas as variaveis dividem o mesmo ''Significado'' podemos fazer dessa forma
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: # No Python, ele conta 0 como um numero par, ja que o resto da divisao dele por 2 é = 0. Entao para ele não contabilizar o 0 podemos adicionar != 0 para que não contabilize o 0 como par
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} numeros pares e {} numeros impares'.format(par, impar))
