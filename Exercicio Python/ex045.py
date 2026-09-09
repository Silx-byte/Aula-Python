'''import random
lista = ['Pedra', 'Papel', 'Tesoura']
print('='*20)
print('Vamos jogar Jokenpo! O famoso Pedra, Papel e Tesoura!')
escolhido = random.choice(lista)
jogo = str(input('Jokenpo! ')).strip().capitalize()
print('Eu escolho {}!'.format(escolhido))
if jogo == escolhido:
    print('Empatamos! Droga, vamos de novo.')
elif jogo == 'Pedra' and escolhido == 'Tesoura':
    print('Voce venceu ! Pedra ganha de Tesoura')
elif jogo == 'Tesoura' and escolhido == 'Papel':
    print('Droga! Voce me venceu !')
elif jogo == 'Papel' and escolhido == 'Pedra':
    print('Droga! Voce me venceu !')
elif jogo == 'Pedra' and escolhido == 'Papel':
    print('HA! Eu te venci!')
elif jogo == 'Tesoura' and escolhido == 'Pedra':
    print('HA! Eu te venci!')
elif jogo == 'Papel' and escolhido == 'Tesoura':
    print('HA! Eu te venci!')
else:
    print('Voce nao sabe jogar ? Vamos tentar de novo!')
print('='*20)'''

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada ? '))
from time import sleep
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POO!!!')
print('-='*11)
print('Computador jogou {}'.format(itens[computador])) # Entre os itens, vai mostrar o que o computador escolheu, por isso esta entre []
print('Jogador jogou {}'.format(itens[jogador])) # Entre os itens, vai mostrar o que o jogador escolheu
print('-='*11)
if computador == 0: # Computador jogou Pedra
    if jogador == 0:
        print('Eu joguei PEDRA também, EMPATAMOS!')
    elif jogador ==1:
        print('VOCE VENCEU!')
    elif jogador == 2:
        print('EU VENCI!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1: # COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('Eu venci!')
    elif jogador == 1:
        print('EMPATAMOS!')
    elif jogador == 2:
        print('Voce Venceu!')
    else:
        print('JOGADA INVALIDA!')

elif computador == 2: # COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('VOCE VENCEU!')
    elif jogador == 1:
        print('EU VENCI')
    elif jogador == 2:
        print('EMPATAMOS')
    else:
        print('JOGADA INVALIDA!')
else:
    print('Jogada INVALIDA')
