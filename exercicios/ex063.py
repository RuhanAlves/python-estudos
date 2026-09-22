n = int(input('Digite um valor: '))
c = 1
futuro = 0
passado, atual = 0, 1
print('\033[1;31m{}\033[m posições do Fibonacci:\n'.format(n))
while c <= n:
    futuro = atual + passado
    print('\033[1;33m{}\033[m'.format(passado), end ='')
    print(' -> ' if c != n else '', end='')
    passado = atual
    atual = futuro
    c += 1
