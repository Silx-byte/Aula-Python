'''print('-'*30)
print('CADASTRE UMA PESSOA')
print('-'*30)
m = f = ''
idade = homem = mulher = idademulher = idade18 = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-'*30)
    if idade >= 18:
        idade18 += 1
    if sexo in 'M':
        homem += 1

    if sexo in 'F':
        if idade < 20:
            idademulher += 1
        mulher += 1

    continuar = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]

    if continuar in 'S':
        continue
    else:
        print('Acabou')
        print(f'Foram {homem} homens, {mulher} mulheres.')
        print(f'Total de pessoas com mais de 18 anos foi {idade18}')
        print(f'{idademulher} mulheres sao menores de 18 anos.')
        break'''

# Resolucao do Professor Guanabara
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' ' # Quando deixamos assim, estamos criando uma variavel para que o while consiga verificar, meio que criando um filtro
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' ' # Lembre-se de SEMPRE deixar um espaco no meio das '', se nao o codiog NAO FUNCIONA
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens cadastrados: {totH}')
print(f'Total de mulheres com menos de 20 anos: {totM20}')

        
