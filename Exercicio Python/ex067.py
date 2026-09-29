n = int(input('Quer ver a tabuada de qual numero ? '))

while not n < 0:
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')
    n = int(input('Qual outro numero você gostaria de ver a tabuada ? '))
    if n < 0:
        print('Acabou!')
        break

# Resolucao do Professor Guanabara

while True:
    num = int(input('Tabuada do numero: '))
    if num < 0:
        break
    print('-'*30)
    for t in range(1, 11):
        print(f'{num} x {t} = {num*t}')
    print('-'*30)
print('Programa Tabuada encerrado!')