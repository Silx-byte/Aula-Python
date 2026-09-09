# d = float(input('Quantos reais voce tem ?'))
# r = d / 3.27
# print ('Com {} reais voce conseguria comprar {:.2f} dolares, e o suficiente ?'.format(d, r))
# print (f'Com R${d} reais voce conseguiria comprar {r:.2f} dolares, e o suficiente ?')

'''produto = float(input("Qual e o preco do produto ? R$"))
x = produto * 0.05
desconto = produto-x
print (f"O produto que custava {produto} agora esta custando {desconto:.0f}")
print('\033[0;30;41m')'''

valor = float(input('Qual o valor do Produto ? RS$ '))
pagamento = int(input('''
[ 1 ] 1x no cartão
[ 2 ] 2x no Cartão
[ 3 ] 3x ou mais no cartão
[ 4 ] Dinheiro ou Chque a vista
Como será a forma de pagamento ? Escolha entre as opções. '''))
if pagamento == 1:
    print('Voce terá 5% de desconto, então a sua compra sairá no valor de {}'.format(valor - (valor *0.05)))
elif pagamento == 2:
    print('A sua compra saira no valor de {} parcelado em duas vezes de {}'.format(valor, valor / 2))
if pagamento >= 3:
    parcela = int(input('Quantas parcelas ? '))
    print('A sua compra saira no valor de {} com juros de 20%, cada parcela sairá no valor de {:.2f}'.format(valor + (valor * 0.2), valor + (valor * 20) / parcela))
elif pagamento == 'dinheiro' or 'cheque':
    print('Sua compra saira no valor de {} com 5% de desconto!')
