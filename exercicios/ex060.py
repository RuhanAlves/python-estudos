'''n = int(input('Digite um número: '))
fatorial = 1
for x in range(n, 0, -1):
    fatorial *= x
print('O número {} tem como valor fatorial: {}'.format(n, fatorial)'''
#Forma de ser feita usando o for

n = int(input('Digite um número: '))
num = n
fatorial = 1
while n > 1:
    fatorial *= n
    n -= 1
print('\033[1;36m{}!\033[m: \033[1;34m{}\033[m'.format(num, fatorial))
#Forma feita através do while