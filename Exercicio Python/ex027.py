'''nome = input('Digite seu nome completo: ')
nome2 = nome.split()
n1 = nome2(0)
n2 = nome2(nome.rfind())
print(f'O nome completo e {nome}, o primeiro nome e {n1} e o ultimo nome e {n2}')'''

# Resolucao do Professor Guanabara

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer')
print('O seu primeiro nome e: {}'.format(nome[0]))
''''print('O seu ultimo nome e: {}'.format(nome[3]))'''
# Dessa maneira so ia funcionar se o nome tivesse 4 cadeias dentro da lista, nao funcionaria para todos.
print('O ultimo nome e: {}'.format(nome[len(nome)-1]))