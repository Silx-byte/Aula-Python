import random
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
print('='*20)