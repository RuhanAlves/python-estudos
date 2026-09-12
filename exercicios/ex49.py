n = int(input('Digite um número: '))
print('\033[34mTABUADA DO NÚMERO \033[1;34m{}\033[m'.format(n))
for num in range (1, 11):
    print('{} x {} = \033[32m{}\033[m'.format(n, num, n*num))