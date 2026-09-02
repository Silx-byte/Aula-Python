a = float(input('Qual e a sua altura ? '))
p = float(input('Quanto voce pesa ? '))
altura = a**2
resultado = p / altura
if resultado < 18.5:
    print('Voce esta abaixo do peso, seu IMC foi de {:.2f}!'.format(resultado))
elif resultado < 25:
    print('Peso ideal! Continue assim, seu IMC foi de {:.2f}'.format(resultado))
elif resultado < 30:
    print('Voce esta em sobrepeso ! Vamos mudar, pois seu IMC foi de {:.2f}!'.format(resultado))
elif resultado < 40:
    print('Voce esta em quadro de OBESIDADE! Seu IMC foi de {:.2f} '.format(resultado))
else:
    print('Voce esta em OBESIDADE MORBIDA! TEMOS QUE MUDAR ISSO URGENTE ! ! Seu IMC foi de {:.2f}'.format(resultado))