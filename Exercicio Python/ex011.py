l = float(input('Largura da parede : '))
alt = float(input('Altura da parede : '))
a = l * alt
print ('A sua parede tem {}metros de altura X {} metros de largura, entao sua area é de {:.1f}m²'.format(alt, l, a))
t = a/2
print('Para pintar toda a sua parede voce vai precisar de {:2}L de tinta'.format (t))
