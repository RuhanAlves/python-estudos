#from math import trunc
#n1 = float(input('Digite um número: '))
#print('O número {} tem como número: inteiro {:.0f}'.format(n1, trunc(n1)))

n1 = float(input('Digite um número: '))
print('O número \033[33m{}\033[m tem como número inteiro: \033[31m{}'.format(n1, int(n1)))