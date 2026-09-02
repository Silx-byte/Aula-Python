# Minha resolucao
'''import random
nr = random.randint(0,5)
tentativa = int(input('Faca seu melhor chute: '))
if tentativa == nr:
    print('Voce acertou!')
else:
    print('Voce errou!')
print('O numero era: {}'.format(nr))'''

# Resolucao do professor Guanabara

from random import randint
from time import sleep # Esse comando serve para adicionar um certo delay no codigo, como se o computador estivesse pensando.
computador = randint(0, 5) # Isso faz o computador "pensar"
print('=' * 20)
print('Vou pensar em um numero de 0 e 5. Tente adivinhar....')
print("=" * 20)
jogador = int(input('Em que numero eu pensei ? ')) # O jogador tenta adivinhar
print('PROCESSANDO....')
sleep(2) # Esse comando vem do (import sleep)
if jogador == computador:
    print('Parabens, voce conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no numero {} e nao no {}!'.format(computador, jogador))

