'''l1 = int(input('Digite um valor: '))
l2 = int(input('Digite outro valor: '))
l3 = int(input('Digite mais um valor: '))
if l1 == l2 == l3:
    print('O triangulo é Equilaterio')
elif l1 == l2 or l2 == l3 or l3 == l1:
    print('O triangulo é Isosceles')
elif l1 != l2 or l2 != l3 or l3 != l1:
    print('O triangulo é Escaleno')
elif l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print('É possivel sim formar um TRIANGULO!')
else:
    print('Voce nao consegue formar um triangulo')'''

# Resolucao do Professor Guanabara:

l1 = float(input('Digite um valor: '))
l2 = float(input('Digite outro valor: '))
l3 = float(input('Digite mais um valor: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print('É possivel sim formar um TRIANGULO')
    if l1 == l2 == l3:
        print('É um Triangulo EQUILATERO')
    elif l1 != l2 and l2 != l3 and l3 != l1:
        print('É um Triangulo ESCALENO!')
    else:
        print('O Triangulo é ISOSCELES!')
else:
    print('Nao pode formar um Triangulo!')
