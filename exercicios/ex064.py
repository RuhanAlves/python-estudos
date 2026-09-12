c = sum = 0
n = int(input('Digite um número [999 para sair]: '))
while n != 999:
    sum += n
    c += 1
    n = int(input('Digite um número [999 para sair]: '))
print('\nForam digitados \033[1;33m{}\033[m números '.format(c), end = '')
print('e a soma de todos eles é de \033[1;31m{}\033[m'.format(sum))