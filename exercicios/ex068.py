from random import randint
c = 0
while True:
    outro = randint(0, 10)
    n = int(input('Digite um valor: '))
    while n < 0 or n > 10:
        n = int(input('Digite um valor: '))
    s = n + outro
    print('\nPar ou Impar? ')
    print(' 1 - [Impar]\n 2 - [Par]')
    esc = int(input('Sua escolha: '))
    while esc < 1 or esc > 2:
        esc = int(input('Sua escolha: '))
    print(f'\nO computador pensou no número \033[2;33m{outro}\033[m')
    print(f'\033[1;33m{n}\033[m + \033[1;36m{outro}\033[m = \033[1;31m{s}\033[m')
    if (s % 2 == 0 and esc == 2) or (s % 2 == 1 and esc == 1):
        print('\033[1;32mVocê venceu, parabéns!\033[m Vamos jogar de novo..\n')
        c += 1
    else:
        print('\033[1;33mVocê perdeu..\033[m\n')
        break
print(f'\033[1;35mGAME OVER!\033[m Você venceu \033[1;31m{c}\033[m vezes.')