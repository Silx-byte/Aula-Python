from time import sleep
# a = str(input('Como posso ajudar ? '))
valor = int(input('O emprestimo seria de quanto ? R$ '))
casa = float(input('Me informe o valor da casa: R$ '))
salario = float(input('Me informe o salario, por favor: R$ '))
tempo = float(input('Me informe tambem em quantos anos voce vai pagar: '))
ano = tempo * 12
parcela = valor / ano
limite = salario * 0.30
if parcela <= limite:
    print('Deixe-me verificar no sistema...')
    sleep(2)
    resposta = input('O valor da parcela ficara em {:.2f}, voce esta de acordo ? '.format(parcela)).strip().lower()
    if resposta == 'nao':
        print('Certo, sentimos muito por nao conseguir ajudar, volte sempre!')
    elif resposta == 'sim':
        print('OTIMO! O emprestimo sera Concedido! Agradecemos pela preferencia.')
    else:
        print('Nao entendi, pode repetir as informacoes novamente ? E no final responda Sim ou Nao por favor.')
if parcela > limite:
    print('Nao podemos conceder o emprestimo desse valor, pois o valor {:.2f} seria mais do que 30% do seu salario! Sentimos muito...'.format(parcela))


# Resolucao do professor do Guanabara.

'''casa = float(input('Valor da casa: R$ '))
salario = float(input('Salario do Comprador: R$ '))
anos = int(input('Quantos anos de financiamento ? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uima casa de R${:.2f} em {} anos'.format (casa, anos), end='')
print('a prestacao sera de {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')'''