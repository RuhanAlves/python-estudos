frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece \033[33m{}\033[m vezes'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição \033[32m{}\033[m'.format(frase.find('A') +1))
print('A última letra A aparece na posição \033[35m{}'.format(frase.rfind('A') +1))