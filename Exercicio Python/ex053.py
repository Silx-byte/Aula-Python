frase = str(input('Digite uma palavra: ')).strip().upper() # strip removendo espaços extras e upper transformando tudo em MAIUSCULO
palavras = frase.split() # o Split faz com que possamos gerar uma lista
junto = ''.join(palavras) # Aqui a gente junta tudo formando 1 só string
inverso = ''
for letra in range(len(junto) -1, -1, -1): # E aqui forma a versão inversa dela mesma
    inverso += junto[letra]
if inverso == junto:
    print('Ele é um PALINDROMO')
else:
    print('Ele NÃO é um PALINDROMO')

