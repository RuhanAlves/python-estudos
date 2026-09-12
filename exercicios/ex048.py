count = 0
soma = 0
for x in range (1, 501, 2):
        if x % 3 == 0:
            soma += x
            count += 1
print('A soma de todos os números múltiplos de 3 ', end='')
print('de um intervalo entre 1 e 500, é \033[32m{}\033[m'.format(soma))
print('\nQuantidade de números que são multiplos de 3: \033[33m{}'.format(count))