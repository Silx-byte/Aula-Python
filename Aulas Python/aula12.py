nome = str(input('Qual e o seu nome ? '))
if nome == 'Paulo':
    print('Que nome Bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Gustavo':
    print('Seu nome e bem popular no Brasil!')
elif nome in 'Ana Claudia Jessica Julia':
    print('Belo nome Feminino')
else:
    print('Seu nome e bem normal!')
print('Tenha um bom dia, {}'.format(nome))
