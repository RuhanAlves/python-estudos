#Exercicio para a conversão de Decimal para Binário, Octal e Hexadecimal
n = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções abaixo:
[ 1 ] \033[1;32mCONVERSOR PARA BINÁRIO\033[m
[ 2 ] \033[1;34mCONVERSOR PARA OCTAL\033[m
[ 3 ] \033[1;33mCONVERSOR PARA HEXADECIMAL\033[m''')
escolha = int(input('Sua escolha: '))
if escolha == 1:
    e = bin(n)
    print('{} para Binário: {}'.format(n, e [2:]))
elif escolha == 2:
    e = oct(n)
    print('{} para Octal: {}'.format(n, e [2:]))
elif escolha == 3:
    e = hex(n)
    print('{} para Hexadecimal: {}'.format(n, e [2:]))
else:
    print('\033[33mEscolha um número válido.\033[m')