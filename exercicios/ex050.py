soma = 0
for x in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
print('\033[34mA soma dos números inteiros pares é \033[1;36m{}\033[m'.format(soma))
