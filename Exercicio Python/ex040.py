'''nota = float(input('Qual foi a primeira nota ? '))
nota2 = float(input('Qual foi a segunda nota ? '))
media = (nota + nota2) / 2
if media < 5:
    print('Aluno Reprovado! Pois sua nota foi de {}'.format(media))
elif media >= 5 and nota <= 6.9:
    print('Voce esta de Recuperacao, pois sua nota foi de {}'.format(media))
else:
    media >=7
    print('Voce esta APROVADO ! ! Sua nota foi de {}'.format(media))'''

# Resoulcao do Professor

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if 7 > media >=5:
    print('Voce esta de Recuperacao')
elif media < 5:
    print('Voce esta REPROVADO!')
elif media >= 7:
    print('O aluno esta APROVADO!')
