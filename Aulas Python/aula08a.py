import math
num = int(input('Digite um numero:'))
raiz = math.sqrt(num)
print ('A raiz de {} e igual a {:.2f}'.format (num, raiz))
print ('O arredondamento para baixo da raiz de {} e igual a {}'.format (num, math.floor(raiz)))
print ('O arredondamento para cima da raiz de {} e igual a {}'.format (num, math.ceil(raiz)))

# Da pra usar o import random
# Usando essa biblioteca, podemos pedir pra ele randomizar numeros.
# Exemplo. 
# import random
# num = random.random()   - ou random.randint(1, 10)
# print(num)

