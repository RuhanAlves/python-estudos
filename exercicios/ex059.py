n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
esc = 0
while esc != 5:
    print('Escolha um dos itens abaixo:')
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair''')
    esc = int(input('\nSua escolha: '))
    if esc == 1:
        print('\033[1;33m{}\033[m + \033[1;33m{}\033[m = \033[1;32m{}\033[m'.format(n1, n2, n1+n2))
    elif esc == 2:
        print('\033[1;33m{}\033[m x \033[1;33m{}\033[m = \033[1;32m{}\033[m'.format(n1, n2, n1*n2))
    elif esc == 3:
        maior = 0
        menor = 0
        if n1 > n2:
            maior = n1
            menor = n2
        else:
            maior = n2
            menor = n1
        print('O número \033[1;32m{}\033[m é maior que o número \033[1;33m{}\033[m.'.format(maior,  menor))
    elif esc == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif esc > 5 or esc < 1:
        print('\nOpção Invalida. Tente novamente\n')
print('\033[1;34mEncerrando...\033[m')