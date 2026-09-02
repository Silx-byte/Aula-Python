'''nome = str(input('Digite um nome: '))
print(f'Nome em Letra Maiuscula: {nome.upper()}')
print(f'Nome em Letra Minuscula: {nome.lower()}')
print(f'Quantas letras tem: {len(nome)}')'''


# Resolucao do Professor Guanabara
# Como colocamos em STR o input, podemos adicionar apos os () o .strip(), que assim ele vai remover os espacos ja contidos na frase e vai apenas mostrar as letras existentes
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em Maiusculo e: {}'.format(nome.upper()))
print('Seu nome em Minusculo e: {}'.format(nome.lower()))
print('O seu nome completo tem {} caracteres'.format(len(nome) - nome.count(' ')))
#print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))

#Pode ser feito tambem dessa forma
separa = nome.split()
print('Seu primeiro nome e {} e seu nome tem {} letras'.format(separa[0], len(separa[0])))

# o split e usado para separar o nome dado em uma Cadeia de Caractere = Paulo Ricardo  ( Paulo Vai virar a Cadeia 0 e o nome Ricardo vira cadeia 1 )
