city = str(input('Digite o nome da cidade: ')).upper().split()
print('A sua cidade começa com Santo? \033[33m{}\033[m'.format('SANTO' in city[0]))
