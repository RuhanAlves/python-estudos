#Exercicio para indicar qual número é maior ou se forem iguais
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O número {} é \033[1;32mmaior\033[m que o número {}.'.format(n1, n2))
elif n2 > n1:
    print('O número {} é \033[1;32mmaior\033[m que o número {}.'.format(n2, n1))
else:
    print('\033[33mNão existe número maior, os dois números são \033[1miguais.\033[m')

