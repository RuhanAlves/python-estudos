from random import randint
nums = ()
maior = menor = 0
for c in range (1, 6):
    x = randint(1, 10)
    if c == 1:
        maior = x
        menor = x
    else:
        if maior < x:
            maior = x
        if menor > x:
            menor = x
    nums = nums + (x,)
print(f'Números gerados: {nums}')
print(f'\nO maior número gerado foi \033[1;32m{maior}\033[m',end = '')
print(f' e o menor foi \033[1;33m{menor}\033[m')
