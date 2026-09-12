#Exercicio para permitir ou não um impréstimo de acordo com as prestações mensais de uma casa que está sendo financiada
print('\033[31m=\033[m' * 10)
print('\033[32mPX BANK\033[m')
print('\033[31m=\033[m' * 10)
valor = float(input('Informe o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Informe em quantos anos você irá pagar a casa: '))
prestacao = valor / (anos * 12)
print('Valor da prestação mensal: \033[1;32mR${:.2f}\033[m'.format(prestacao))
print('Limite permitido conforme o salário: \033[1;35mR${:.2f}\033[m'.format(salario * 0.3))
if (salario * 0.3) < prestacao:
    print('\033[33mValor \033[4mexcedido\033[m \033[33mde 30% do salário.\033[m \033[1;35mNão é possivel fazer o empréstimo.\033[m')
else:
    print('\033[32mEmpréstimo permitido.\033[m')
print('\033[36mTenha um bom dia!\033[m')
