real = float(input('Digite um valor em real: R$'))
dolar = 5.19
Euro = 5.89
Ieni = 0.032
print('\nQuantidade que pode-se comprar em:\nDolar: \033[32m$\033[m{:.2f}'.format(real/dolar))
print('Euro:  \033[36m€\033[m{:.2f}'.format(real/Euro))
print('Ieni:  \033[33m¥\033[m{:.2f}'.format(real/Ieni))