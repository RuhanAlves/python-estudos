maiorPeso = 0
menorPeso = 0
for x in range (1, 6):
    Peso = float(input('Digite o peso da {}ª pessoa: '.format(x)))
    if x == 1:
        maiorPeso = Peso
        menorPeso = Peso
    if Peso > maiorPeso:
            maiorPeso = Peso
    elif menorPeso > Peso:
            menorPeso = Peso
print('O maior peso lido foi {}Kg'.format(maiorPeso))
print('O menor peso lido foi {}Kg'.format(menorPeso))