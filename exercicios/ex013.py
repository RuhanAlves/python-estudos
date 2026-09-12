salario = float(input('Digite o valor do salário: R$'))
aumento = salario + (salario * 0.15)
print('Aumento de \033[32m15%\033[m do salário, valor total: \033[34mR${:.2f}'.format(aumento))