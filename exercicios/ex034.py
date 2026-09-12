#Exercicio para analsiar se um salário vai ter aumento de 10% ou 15%
salario = float(input('Digite um salário a receber aumento: '))
if salario > 1250:
    salario += salario * 0.10
    print('Aumento de \033[32m10%\033[m no salário')
    print('Salário com aumento: \033[33mR${:.2f}\033[m'.format(salario))
else:
    salario += salario * 0.15
    print('Aumento de \033[32m15%\033[m no salário')
    print('Salário com aumento: \033[33mR${:.2f}'.format(salario))