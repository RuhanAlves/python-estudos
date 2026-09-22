cont = 0
print('\033[33mNúmeros pares de 1 a 50:\033[m')
#for x in range (1, 51)
    #if x % 2 == 0:
for x in range (2, 51, 2):
    cont += 1
    print(x)
print('Existem \033[1;34m{} números\033[m pares entre 1 e 50.'.format(cont))