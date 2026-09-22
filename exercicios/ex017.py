from math import hypot
catO = float(input('Digite o valor do Cateto Oposto: '))
catA = float(input('Digite o valor do Cateto Adjacente: '))
hip = hypot(catO, catA)
print('\n\033[7;31mA soma dos quadrados dos Catetos é igual ao quadrado da hipotenusa.\033[m')
print('O valor da hipotenusa é: \033[7m{:.2f}\033[m'.format(hip))
