#Exercicio para calcular o IMC de uma pessoa e classificá-la
peso = float(input('Digite o seu peso (kg): '))
altura = float(input('Digite a sua altura: '))
IMC = peso / (altura ** 2)
print('IMC do usuário de {}'.format(IMC))
if IMC < 18.5:
    print('\033[34mAbaixo do peso\033[m')
elif IMC < 25:
    print('\033[32mPeso ideal\033[m')
elif IMC < 30:
    print('\033[33mSobrepeso\033[m')
elif IMC < 40:
    print('\033[35mObesidade\033[m')
else:
    print('\033[31mObesidade mórbida\033[m')