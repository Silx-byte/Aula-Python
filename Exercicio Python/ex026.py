'''frase = str(input('Digite uma frase: ')).strip().lower()
nc = frase.count('a')
nf = frase.find('a')
print('A letra A aparece {} vezes'.format(nc))
print('A letra A apareceu na posicao {}'.format(nf))'''

# Resolucao do Professor Guanabara

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A apareceu {} vezes na frase'.format(frase.count('A')))
print('A letra A apareceu na posicao {}'.format(frase.find('A')+1)) # Ele utilizou o +1 para colocar na posicao que nos vemos pois no Python, como ele comeca a contar pelo 0, entao seria numa posicao diferente da que estamos vendo
print('A ultima letra A apareceu na posicao {}'.format(frase.rfind('A')+1))
