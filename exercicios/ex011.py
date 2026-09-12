H = float(input('Altura em metros da parede: '))
L = float(input('Largura em metros da parede: '))
A = H * L
print('\nDimensões da parede: {:.2f}m x {:.2f}m = \033[34m{:.2f}m²\033[m'.format(H,L,A))
print('Quantidade de tinta necessária para pintar a parede: \033[36m{:.2f}L'.format(A/2))
