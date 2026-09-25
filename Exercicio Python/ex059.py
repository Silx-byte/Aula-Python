'''valor = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
print([ 1 ] somar # Para funcionar novamente, precisa colocar as Aspas
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos numeros
[ 5 ] sair do programa)
escolha = int(input('Digite a opção desejada: '))
if escolha == 1:
    resultado = valor + valor2
    print(resultado)
if escolha == 2:
    resultado = valor * valor2
    print(resultado)
if escolha == 3:
    if valor > valor2:
        print(valor)
    else:
        print(valor2)
if escolha == 4:
    valor = int(input('Digite um novo valor: '))
    valor2 = int(input('Digite mais um valor: '))
if escolha == 5:
    print('Obrigado, volte sempre.')'''


# Resolução do Professor:

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
opção = 0
while opção != 5: # Com esse while, ele vai ficar mostrando o menu até a gente digitar o 5. E podemos fazer varias operações com os numeros escolhidos.
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opção = int(input('Qual é a sua opção ?: '))
    if opção == 1:
        soma = n1 + n2
        print('O resultado é {}'.format(soma))
    elif opção == 2:
        multiplicação = n1 * n2
        print('O resultado da multiplicação é {}'.format(multiplicação))
    elif opção == 3:
        if n1 < n2:
            maior = n2
        if n2 < n1:
            maior = n1
        print('O maior é {}'.format(maior))
    elif opção == 4:
        print('Informe os valores novamente: ')
        n1 = int(input('Informe o primeiro valor: '))
        n2 = int(input('Informe o segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção invalida.')
    print('=-='*10)
print('Fim do Programa. Volte sempre!')