'''import math
ang = float(input("Insira um Angulo: "))
radi = math.radians(ang)
tang = math.tan(radi)
cos = math.cos(radi)
seno = math.sin(radi)
print (f"O angulo {ang} tem a {tang}, o cosseno em {cos} e o seno em {seno}")'''

# Resolucao do Professor Guanabara \/

import math
angulo = float(input("Insira um Angulo: "))
seno = math.sin(math.radians(angulo))
print (f"O angulo de {angulo} tem o SENO de {seno:.2f}")
cosseno = math.cos(math.radians(angulo))
print (f"O angulo de {angulo} tem o COSSENO de {cosseno:.2f}")
tangente = math.tan(math.radians(angulo))
print (f"O angulo de {angulo} tem a TANGENTE de {tangente:.2f}")


