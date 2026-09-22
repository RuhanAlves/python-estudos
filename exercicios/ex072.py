nome = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoite', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if num >= 0 and num <= 20:
        break
print(f'\nVocê digitou o número {nome[num]}')
