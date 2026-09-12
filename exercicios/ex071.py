valor = int(input('Valor a ser sacado: R$'))
print('Troco: ')
c50 = valor // 50
valor %= 50
c20 = valor // 20
valor %= 20
c10 = valor // 10
valor %= 10
c1 = valor // 1
valor %= 1
if c50 > 0:
    print(f'\033[1;33m{c50}\033[m cédulas de R$50.00')
if c20 > 0:
    print(f'\033[1;33m{c20}\033[m cédulas de R$20.00')
if c10 > 0:
    print(f'\033[1;33m{c10}\033[m cédulas de R$10.00')
if c1 > 0:
    print(f'\033[1;33m{c1}\033[m cédulas de R$1.00')
