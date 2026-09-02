distancia = int(input("Qual a distancia da viajem que voce vai fazer ? "))
if distancia <=200:
    print('Voce vai pagar {:.2f} reais'.format(distancia * 0.5))
else:
    print('Voce vai pagar {:.2f} reais'.format(distancia * 0.45))

# Podendo ser feito tambem de maneira simplificada:
# preco = distancia * 0.50 if distancia <=200 else distancia * 0.45