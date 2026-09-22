#Analise de números ímpares e pares
n1 = int(input('Digite um número qualquer inteiro: '))
if n1 % 2 == 0:
    print('O número \033[33m{}\033[m é \033[34mpar\033[m'.format(n1))
else:
    print('O número \033[31m{}\033[m é \033[34mimpar\033[m'.format(n1))