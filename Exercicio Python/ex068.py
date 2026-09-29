from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'IP':
        tipo = str(input('Impar ou Par ? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total foi {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce ganhou !')
            v += 1
        else:
            print('Voce perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você ganhou!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar de novo')
print(f'Você ganhou {v} vezes!')
    
            