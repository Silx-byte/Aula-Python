n1 = int(input('Digite um Valor'))
n2 = int(input('Digite a razao'))
for c in range(n1, 20, n2):
    print(c)


# Resolucao do Professor Guanabara

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end = ' ')
print('Acabou!')