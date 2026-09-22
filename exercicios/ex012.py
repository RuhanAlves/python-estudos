produto = float(input('Digite o valor do produto: R$'))
desconto = produto - (produto * 0.05)
print('Produto com \033[35m5%\033[m de desconto, valor total: \033[32mR${:.2f}\033[m'.format(desconto))