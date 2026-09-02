# Minha resolucao
'''velocidade = float(input('Qual velocidade voce passou na Avenida Brasil ? '))
multa = (velocidade - 80) * 7
if velocidade >=80:
    print('Voce ultrapassou o limite de Velocidade, voce tera que pagar {:.1f} reais de multa '.format(multa))
else:
    print('Voce esta dentro do limite de velocidade! ')'''

# Resolucao do Professor Guanabara
velocidade = float(input('Qual e a velocidade atual do carro ? '))
if velocidade > 80:
    print('MULTADO! Voce excedeu o limite permitido que e de 80Km/hr')
    multa = (velocidade - 80) * 7
    print('Voce deve pagar uma muta de {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com seguranca!')

