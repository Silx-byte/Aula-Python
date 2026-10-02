print('-'*30)
print('LOJAS AMERICANAS')
print('-'*30)
total = menor = totmil = cont = 0 # Nesse caso precisamos de um contador para saber quantos procutos nós temos e qual é o primeiro produto também. Por isso adicionamos o CONT.
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preco: R$ '))
    cont += 1 # A cada produto adicionado, ele vai adicionar +1
    total += preco
    if preco >= 1000:
        totmil += 1
    if cont == 1: # Se for o primeiro produto, o menor preço passa a ser o preço que foi colocado.
        menor = preco
        barato = produto
    else: # Caso nao seja o primeiro produto, precisamos verificar se o menor vai ser menor que o preço. Montando um filtro para saber qual realmente é o menor e salvar a informação
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar ? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('{:-^40}'.format(' FIM DO PROGRAMA! '))
print(f'Total da compra foi: R$ {total:.2f}')
print(f'Temos {totmil} produtos costumando mais de R$1000.00')
print(f'O produto mais barato foi {barato}, que custou {menor:.2f}')