n1 = int(input('Digite um número: '))
antes = n1 - 1
depois = n1 + 1
cores = {'AzulClaro': '\033[36m',
         'Azul': '\033[33m',
         'Limpa': '\033[m'}
print ('Seu antecessor: {}{}{}, seu sucessor: {}{}'.format(cores['AzulClaro'], antes, cores ['Limpa'], cores ['Azul'], depois))