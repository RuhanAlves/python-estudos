#Exercicio para analisar quando deverá ser pago de acordo com km rodados
distancia = int(input('Digite a distância da viagem em km: '))
if distancia <= 200:
    print('\033[4mR$0,50 por km rodado em viagem\033[m')
    print('Total a pagar: \033[1;35mR${:.2f}\033[m'.format(distancia*0.50))
else:
    print('\033[4mViagem longa. R$0,45 por km rodado\033[m')
    print('Total a pagar: \033[1;35mR${:.2f}'.format(distancia*0.45))