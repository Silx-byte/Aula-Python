'''import math
cata = float(input("Qual e o tamanho do cateto oposto?"))
cato = float(input("Qual e o tamanho do cateto adjacente?"))
rh = (cata ** 2 + cato ** 2) ** (1/2)
print (f"a hipotenusa vai medir{rh:.2f}")'''

'''import math
cata = float(input("Qual e o tamanho do cateto oposto?"))
cato = float(input("Qual e o tamanho do cateto adjacente?"))
rh = (cata ** 2 + cato ** 2)
print (f"A hipotenusa vai medir {math.sqrt(rh)}")'''

import math
co = float(input("Comprimento do cateto oposto:"))
ca = float(input("Comprimento do cateto adjacente:"))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))



