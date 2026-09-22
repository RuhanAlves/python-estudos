c = soma = maior = menor = 0
esc = 'S'
while esc == 'S':
    n = int(input('Digite um número: '))
    if c == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
    c += 1
    esc = str(input('Quer continuar? [S]/[N] ')).upper().strip()[0]
print('\nMédia total: \033[1;33m{:.2f}\033[m'.format(soma/c))
print('Maior número: \033[1;32m{}\033[m'.format(maior))
print('Menor número: \033[1;36m{}\033[m'.format(menor))
