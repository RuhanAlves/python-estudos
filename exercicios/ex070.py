MaisBarato = ''
s = MaisDe1000 = c = MenosCaro = 0
while True:
    nome = str(input('Digite o nome do produto: '))
    valor = float(input('\nValor do produto: R$'))
    if c == 0 or valor < MenosCaro:
        MenosCaro = valor
        MaisBarato = nome
    if valor > 1000:
        MaisDe1000 += 1
    s += valor
    esc = ' '
    while esc not in 'SsNn':
        esc = str(input('\nDeseja continuar? [S/N]: ')).strip()[0]
    if esc in 'Nn':
        break
    c += 1
    print('')
print(f'\nTotal gasto na compra: \033[1;35mR${s:.2f}\033[m')
print(f'Quantidade de produtos acima de R$1000: \033[1;31m{MaisDe1000}\033[m')
print(f'O produto mais barato foi \033[1;36m{MaisBarato}\033[m que custou \033[1;32mR${MenosCaro:.2f}\033[m')
