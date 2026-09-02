'''import random
pa = input("Primeiro Aluno: ")
sa = input ("Segundo Aluno: ")
ta = input ("Terceiro Aluno: ")
qa = input ("Quarto Aluno : ")
lista = [pa, sa, ta, qa]
print (f"O aluno escolhido foi {random.choice(lista)}")'''

# Resolucao do Professor Guanabara

import random
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

