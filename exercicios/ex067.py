from time import sleep
while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    print(f'Tabuada do número \033[1;31m{n}\033[m:')
    for c in range (1, 11):
        print(f'\033[1;33m{n}\033[m x \033[1;36m{c}\033[m = \033[1;31m{n*c}\033[m')
print('\033[1;34mEncerrando\033[m', end='')
sleep(0.5)
print('\033[1;34m.\033[m', end='')
sleep(0.8)
print('\033[1;34m.\033[m', end='')
