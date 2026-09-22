#Exercicio para multa de carros acima de 80km/h
velocity = float(input('Digite a velocidade do carro: '))
if velocity > 80:
    multa = velocity - 80
    print('\033[33mVelocidade limite ultrapassada\033[m')
    print('Multa a pagar: \033[1;35mR${:.2f}\033[m'.format(multa * 7))
print('\033[31mTenha um bom dia e dirija com segurança!')