# 5+2 == 7
# 5-2 == 3
# 5*2 == 10
# 5/2 == 2.5
# 5**2 == 25
# 5//2 == 4
# 5%2 == 1 
# Existe tambem a raiz quadrada Exemplo: 81**(1/2)  Sendo a raiz quadrada ( **(1/2)
# Ordem de precedencia - 1 PARENTESES () 2- POTENCIA ** 3- MULTIPLICACAO, DIVISAO, DIVISAO INTEIRA, RESTO DA DIVISAO * / // % 4- SOMA E SUBTRACAO + - 
n1 = int(input('Um valor'))
n2 = int(input('Outro valor'))
s= n1+n2
m= n1*n2
d= n1/n2
di= n1//n2
e= n2**n2
print('A soma vale {}, o produto e {} e a divisao e {:.2f}'.format(s,m,d))
print('A divisao inteira {} e a potencia {}'.format(di, e))


# Se eu quiser que aja uma quebra na linha eu posso colocar \n 
# Se eu precisar digitar um outro PRINT e nao quiser que quebre a linha, ou seja, que todas as informacoes aparecam na primeira linha, eu coloco end= '' no final da primeira linha
# Exemplo : 
# print('A soma vale {}, o produto e {} e a divisao e {:.2f}'.format(s,m,d), end= '')
#print('A divisao inteira {}  e a potencia {}'.format(di, e))

