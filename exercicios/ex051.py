prim = int(input('Informe o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
print('\n\033[33m1º TERMO DA PA \033[1;34m{}\033[m \033[33mATÉ O SEU 10º TERMO:\033[m'.format(prim))
for x in range(prim, prim + (r * 10), r):
    if x < prim + (r * 9):
        print(x, end='')
        print(' ->', end=' ')
    else:
        print(x, end='')
