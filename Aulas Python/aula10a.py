'''tempo = int(input('Quantos anos tem seu carro ?'))
print('Carro Novo' if tempo<=3 else'Carro Velho') # Podemos simplificar tudo em uma so linha.
print('--FIM--')
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print ('--FIM--')'''

# Continuacao da aula 10

'''nome = str(input('Qual e o seu nome ?'))
if nome == 'Paulo':
    print('Que lindo nome voce tem!')
else:
    print('Seu nome e tao normal!')
print('Bom dia, {}!'.format(nome))'''

# Continuacao da aula 10

n1 = float(input('Qual a primeira nota do aluno: '))
n2 = float(input('Qual a segunda nota do aluno: '))
m = (n1 + n2)/2
print('A media do Aluno foi {}'.format(m))
if m >=6:
    print('Voce passou!')
else:
    print('Voce reprovou!')

# Podendo simplificar da seguinte forma (As vezes nao e recomendado)
# print('Voce Passou!' if >=6 else 'Estude mais !')