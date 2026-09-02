# Minha resolucao
'''ano = int(input('Fale um ano e eu direi se ele e um ano bissexto ou nao: '))
if ano % 4 == 0:
    print('Ele e um ano bissexto')
else: 
    if ano % 400 == 0:
        print('Ele e um ano bissexto')
    else:
        print('Ele nao e um ano bissexto')'''
        

# Resolucao do professor Guanabara

# Ele usou um novo comando chamado datetime, ele importou essa biblioteca para informar pegar o ano registrado no PC
from datetime import date
ano = int(input('Que ano quer Analisar ? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano {} e um ano BISSEXTO'.format(ano))
else:
    print('O ano {} NAO e BISSEXTO'.format(ano))
