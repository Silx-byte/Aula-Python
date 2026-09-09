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

# Resolucao do Professor Guanabara
peso = float(input('Qual é o seu peso ? (Kg)'))
altura = float(input('Qual é a sua altura ? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Parabens! Voce esta na faixa de peso normal.')
elif 25 <= imc < 30:
    print('Voce esta em SOBREPESO!')
elif  imc >= 40:
    print('Voce esta em OBSEIDADE MORBIDA ! Cuidado ! ! ')
