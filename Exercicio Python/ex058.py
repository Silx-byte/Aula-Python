from random import randint
computador = randint(0, 10)
palpite = 0
jogador = int(input('Tente adivinhar no numero que estou pensando: '))
while jogador != computador:
    print('Você errou!')
    palpite += 1
    jogador = int(input('Tente novamente: '))
    if jogador == computador:
        print('Você acertou ! Eu estava pensando no numero {}, foram necessarias {} tentativas'.format(computador,palpite))