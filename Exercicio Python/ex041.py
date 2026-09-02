from datetime import date
ano = date.today().year
nascimento = int(input('Em que ano voce nasceu ? '))
idade = ano - nascimento
print('Voce tem {} de idade!'.format(idade))
if idade <=9:
    print('Voce esta classificado como MIRIM! Parabens')
elif idade <=14 and idade >9:
    print('Voce esta classificado como INFANTIL! Parabens!')
elif idade <=19 and idade >14:
    print('Voce esta classificado como JUNIOR! Parabens!')
elif idade <=20 and idade >19:
    print('Voce esta classificado como SENIOR! Parabens!')
else:
    idade > 20
    print('Voce esta classificado como MASTER! Parabens!')