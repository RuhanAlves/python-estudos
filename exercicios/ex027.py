nome = str(input('Digite seu nome completo: ')).strip().split()
print('Primeiro nome: \033[1;31m{}\033[m'.format(nome [0]))
print('Último nome: \033[1;34m{}'.format(nome [-1]))