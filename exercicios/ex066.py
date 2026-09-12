c = soma = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    soma += n
    c += 1
print(f'Foram digitados \033[1;31m{c}\033[m números', end='')
print(f' e a soma de todos os valores é \033[1;36m{soma}\033[m')