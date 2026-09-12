div = 0
n = int(input('Digite um número: '))
for x in range (1, n +1):
    if n % x == 0:
        print('\033[33;1m{}\033[m'.format(x), end= ' ')
        div += 1
    else:
        print('\033[35m{}\033[m'.format(x), end= ' ')
print('\n\nO número \033[36m{}\033[m tem \033[33m{}\033[m divisores'.format(n, div))
if div == 2:
    print('E por isso ele \033[1;32mÉ\033[m um número primo.'.format(n))
else:
    print('E por isso ele \033[1;35mNÃO\033[m é um número primo.'.format(n))