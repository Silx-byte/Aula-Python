salario = float(input('Qual e o seu salario ? R$'))
if salario >= 1250:
    print('Voce recebera um aumento de 10%, entao seu salario vai para {}'.format(salario + (salario * 0.1) ))
else:
    print('Voce recebera um aumento de 15%, entao seu salario vai para {}'.format(salario + (salario * 0.15)))
print ('Parabens pelo Aumento ! !')

# Resolucao do Professor Guanaraba:

salario = float(input('Qual e o salario do funcionario ? R$ '))
if salario <=1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${} agora.'.format(salario, novo))
