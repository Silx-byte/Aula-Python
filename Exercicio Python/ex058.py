'''from random import randint
computador = randint(0, 10)
palpite = 0
jogador = int(input('Tente adivinhar no numero que estou pensando: '))
while jogador != computador:
    print('Você errou!')
    palpite += 1
    jogador = int(input('Tente novamente: '))
    if jogador == computador:
        print('Você acertou ! Eu estava pensando no numero {}, foram necessarias {} tentativas'.format(computador,palpite))'''


# Resolução do Professor Guanabara

from random import randint
computador = randint(0,10)
print('Sou seu computador, acabei de pensar em um numero entre 0 e 10.')
print('Sera que você consegue adivinhar qual foi ? ')
acertou = False
palpites = 0
while not acertou: #Em Portugol fica - Enquanto não acertou
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} palpites'.format(palpites))