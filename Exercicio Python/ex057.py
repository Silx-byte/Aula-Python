sexo = str(input('Sexo: [M/F]')).strip().upper()
while not sexo in 'MF':
    print('Digite novamente')
    sexo = str(input('Sexo: [M/F]')).strip().upper()
print('Acabou')