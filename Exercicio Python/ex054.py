from datetime import date
atual = date.today().year
acima = 0
abaixo = 0
for c in range(1, 8):
    ano = int(input('Digite o ano do seu nascimento: '))
    if atual - ano >= 21:
        acima = acima + 1
    else:
        abaixo = abaixo +1
print('A quantidade de pessoas acima de 18 anos foi {} e a quantidade de pessoas abaixo foi {}'.format(acima, abaixo))