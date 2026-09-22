prod = ('Ovos', 5.50, 'Maça', 2.25, 'Leite', 6.78, 'Biscoito', 7.99,
        'Coração humano', 00.00)
print(f'-' * 40)
print(f'{"PRODUTOS DA LOJA DO GULOSINHO!!":^40}')
print(f'-' * 40)
for pos in range (0, len(prod)):
    if pos % 2 == 0:
        print(f'{prod[pos]:.<30}', end = '')
    else:
        print(f'R${prod[pos]:.2f}')