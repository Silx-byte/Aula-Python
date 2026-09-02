'''from datetime import date
ano = date.today().year
nascimento = int(input('Em que ano voce nasceu ? '))
idade = ano - nascimento
alistamento = nascimento + 18
if idade > 18:
    print('Ja passou o tempo de se alistar, voce deveria ter se alistado em {}!'.format(alistamento))
elif idade < 18:
    print('Voce precisa se alistar em {} anos'.format(18 - idade))
else:
    print('E hora de voce se alistar ! Se conduza ate o posto do exercito mais proximo ! Boa sorte')'''

# Resulucao do Guanabara

from datetime import date
atual = date.today().year
nasc = int(input('Em que ano voce nasceu ? '))
sex = input('Sexo ? [M] ou [F]').strip().capitalize()
idade = atual - nasc
if sex == 'F':
    print('Voce nao precisa se alistar') end=""
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Voce TEM que se alistar IMEDIATAMANTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o Alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce deveria ter se alistado ha {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))


