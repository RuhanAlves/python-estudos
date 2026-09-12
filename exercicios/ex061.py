a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 1
print('\n10 primeiros termos da PA:\n')
while c <= 10:
    print('\033[1;33m{}\033[m'.format(a1), end = '')
    print(' -> ' if c != 10 else '', end = '')
    a1 += r
    c += 1