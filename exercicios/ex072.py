nome = 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoite', 'dezenove', 'vinte'
num = int(input('Digite um número de 0 a 20: '))
while num < 0 or num > 20:
    num = int(input('Digite um número de 0 a 20: '))
num -= 1
print(f'Você digite o número {nome[num]}')
