a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))
c = int(input("Digite mais um valor: "))
if a + b > c:
    if a + c > b:
        if b + c > a:
            print('Voce consegue sim formar um triangulo')
        else:
            print('Voce nao consegue formar um triangulo')
    else:
        print('Voce nao consegue formar um triangulo')
else:
    print('Voce nao consegue formar um triangulo')


print('='*20)
print('Analisador de Triangulos')
print('='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos PODEM formar um triangulo!')
else:
    print('Os segmentos NAO PODEM formar um triangulo!')