'''valor = float(input('Qual o valor do Produto escolhido ? '))
dinheiro = valor - (valor * 0.1)
cartao = valor - (valor *0.05)
x2 = valor / 2
x3 = valor + (valor * 0.2) / 3
resposta = input(f'Certo, e como sera a forma de pagamento ? O valor saira {valor}. \nAceitamos Dinheiro ou Cheque com desconto ate 10%, ou 1 vez no cartao tem 5%, \nPodemos parcelar tambem em 2x sem juros ou em ate 3x com 20% de juros. ').strip().lower()
if resposta == 'dinheiro' or resposta == 'cheque':
    print('Certo, a sua compra ficara no valor de {}'.format(dinheiro))
elif resposta == 'cartao':
    print('Certo! A sua compra ficara no valor de {}.'.format(cartao))
elif resposta == '2x':
    print('Certo! A sua compra ficara em duas parcelas de {}'.format(x2))
elif resposta == '3x':
    print('Certo! A sua compra tera uma adicao de 20% de juros, voce tera que pagar 3 parcelas de {}.'.format(x3))'''

# Resolucao do Professor Guanabara
# Podemos usar a formatacao .format Para organizarmos os prints e o que vai aparecer na tela, segue o exemplo abaixo:
print('{:=^40}'.format('LOJAS PAULINHO'))
preço = float(input('Preço das Compras R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no Cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção ?'))
if opcao == 1:
    total = preço - (preço * 0.1)
elif opcao == 2:
    total = preço - (preço *0.05)
elif opcao == 3:
    total = preço
    parcela = preço / 2
    print('Ficará no valor de R${} e o valor da parcela ficara em 2x de {:.2f}. '.format(preço, parcela))
elif opcao == 4:
    total = preço + (preço * 20 / 100)
    totalparcela = int(input('Quantas parcelas voce gostaria ? '))
    parcela = total / totalparcela
    print('A sua compra será parcelada em {}x de {:.2f} COM JUROS!'.format(totalparcela, parcela))
# Podemos criar variaveis dentro dos ELIFS para organizar e realizar atividades que só acontecerao quando o codigo precisar passar por esses elifs.
print('O valor da compra que seria {} vai terminar no valor de {}!'.format(preço, total))
