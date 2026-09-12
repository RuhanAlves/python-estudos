a1 = int(input('Digite o número do primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
aTodos = a1
c = 0
total = 0
print('\033[1;31m10\033[m primeiros termos da PA \033[1;31m{}\033[m\n'.format(aTodos))
while c <= 9:
    print('\033[1;33m{}\033[m'.format(a1), end = '')
    print(' -> ' if c != 9 else '', end= '')
    a1 += r
    c += 1
total += c
opcao = int(input('\n\nQuantos termos a mais deseja? '))
while opcao != 0:
    c = opcao
    total += c
    print('\nMais \033[1;33m{}\033[m termos da PA \033[1;36m{}\033[m: \n'.format(opcao, aTodos))
    while c >= 1:
        print('\033[1;33m{}\033[m'.format(a1), end='')
        print(' -> ' if c != 1 else '', end='')
        a1 += r
        c -= 1
    opcao = int(input('\n\nQuer mais quantos termos? '))
print('\nForam digitados {} termos no total'.format(total))
print('\n\033[1;34mEncerrando...\033[m')
