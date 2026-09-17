'''media = 0
for c in range(0, 4):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = input('Você é do Sexo Masculino [ M ] ou do Sexo Feminino [ F ] ? ').strip().upper()
    media = (media + idade) / 4
    maior = 0
    mulheres = 0
    if sexo == 'F' and idade < 20:
        mulheres += 1
    elif sexo == 'M' and idade > maior:
        idade == maior
        if idade == maior:
            velho = nome
print('Existem {} mulheres abaixo de 20 anos ')
print('O homem mais velho tem {} e se chama {}'.format(maior, velho))
    
        
print(nome, idade, sexo, media)'''

# Resolução Professor Guanabara
somaidade = 0
nomevelho = '' # Sempre que eu quiser salvar alguma informação em Texto, podemos criar a variavel e deixar em ''
maioridadehomem = 0
somaidade = 0
totalmulher20 = 0
for p in range(1, 5):
    print ('-'*4,'{} PESSOA'.format(p),'-'*4)
    nome = str(input('Digite seu nome: ')).strip().capitalize()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip().capitalize()
    somaidade += idade
    if p == 1 and sexo == 'M': # Isso é utilizado quando na variavel SEXO existe algo que deixe a opção que o usuario colocar como MAIUSCULO, caso não queira, podemos utilizar também o in 'Mm'. Que assim ele vai considerar as duas opções de M
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem: # O de cima é utilizado para colocar um valor dentro da variavel, e essa agora serve para substituir caso encontre algum valor maior.
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totalmulher20 += 1 
mediaidade = somaidade / 4
print('A media de idade do grupo é de {}'.format(mediaidade))
print('O homem mais velho tem {} e se chama {}'.format(maioridadehomem, nomevelho))
print('A quantidade de mulheres que estão abaixo de 20 anos são {}'.format(totalmulher20))
