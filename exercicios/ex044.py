#Exercicio para calcular valor de um problema conforme determinada forma de pagamento
prod = float(input('Digite o valor da compra: R$'))
print('''Escolha uma das opções abaixo:
[ 1 ] \033[1;32mDINHEIRO/CHEQUE\033[m
[ 2 ] \033[1;33mCARTÃO À VISTA\033[m
[ 3 ] \033[1;34m2x NO CARTÃO\033[m
[ 4 ] \033[1;36m3x OU MAIS NO CARTÃO\033[m''')
paga = int(input('Sua escolha: '))
if paga == 1:
    print('\033[1;32m10% de desconto\033[m na compra. ', end='')
    print('\033[34mValor total final: \033[1;34mR${:.2f}\033[m'.format(prod - prod * 0.1))
elif paga == 2:
    print('\033[1;32m5% de desconto\033[m na compra. ', end='')
    print('\033[mValor total final: \033[1;34mR${:.2f}\033[m'.format(prod - prod* 0.5))
elif paga == 3:
    parc = prod / 2
    print('\033[34mSua compra foi parcelada em 2x de \033[1;34mR${:.2f}\033[m'.format(parc))
elif paga == 4:
    parc = int(input('Parcelado em quantas vezes? '))
    total = prod + prod * 0.2
    divid = total / parc
    print('Compra parcelada em {}x, '.format(parc), end='')
    print('de \033[1;35mR${:.2f}\033[m por parcela.'.format(divid))
    print('\033[1;35m20% de Juros\033[m na compra. ', end='')
    print('\033[34mValor total final: \033[1;34mR${:.2f}\033[m'.format(total))
else:
    print('\033[33mSelecione uma opção válida.\033[m')