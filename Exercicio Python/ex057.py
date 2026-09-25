'''sexo = str(input('Sexo: [M/F]')).strip().upper()
while not sexo in 'MF':
    print('Digite novamente')
    sexo = str(input('Sexo: [M/F]')).strip().upper()
print('Acabou')'''

# Resolucao do Professor

sexo = str(input('Digite seu sexo: ')).strip().upper()[0]# Podemos usar [0] para que o Upper pegue apenas a PRIMEIRA LETRA
while sexo not in 'MmFf': # Traducao em Portugol - enquanto sexo nao estiver em '':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))