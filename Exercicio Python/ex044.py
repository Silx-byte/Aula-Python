valor = float(input('Qual o valor do Produto escolhido ? '))
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
    print('Certo! A sua compra tera uma adicao de 20% de juros, voce tera que pagar 3 parcelas de {}.'.format(x3))
