from time import sleep
from random import randint
num = randint(0,10)
print('Olha, o computador vai pensar um número de 1 a 10, tenta adivinhar.')
print('Calma ai', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
user = int(input('\nBeleza, Tenta adivinhar o número que o computador pensou: '))
tentativas = 1
while user != num:
    if num > user:
        user = int(input('Hm... é mais, tenta denovo: '))
    elif num < user:
        user = int(input('Hm... é menos, tenta denovo: '))
    tentativas += 1
print('\033[1;34mParabéns, você conseguiu acertar!\033[m')
print('Foram \033[1;33m{}\033[m tentativas até acertar o número \033[1;36m{}\033[m'.format(tentativas, num))