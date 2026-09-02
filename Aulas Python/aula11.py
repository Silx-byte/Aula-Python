'''a = 3
b = 5
print('Os valores sao \33[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))'''

nome = 'Paulo'
cores = {'limpa':'\033[m',
        'azul' :'\033[34m', 
        'amarelo' :'\033[33m', 
        'pretoebranco' :'\033[7:30'}
# print('Ola! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
print('Ola! Muiito prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))
