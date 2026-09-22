from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10), )
print(f'Valores sorteado: {numeros}')
print(f'\nMaior valor sorteado: {max(numeros)}')
print(f'\nMenor valor sorteado: {min(numeros)}')
