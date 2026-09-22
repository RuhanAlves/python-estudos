nome = str(input('Digite o seu nome: ')).upper().strip()
print('O seu nome tem Silva nele? \033[31m{}'.format('SILVA' in nome))