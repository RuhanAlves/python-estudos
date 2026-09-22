km = int(input('Informe a quantidade de Km rodados: '))
dias = int(input('Digite a quantidade de dias alugados: '))
Total = (dias * 60) + (km * 0.15)
print('Preço a pagar: \033[1;35mR${:.2f}'.format(Total))