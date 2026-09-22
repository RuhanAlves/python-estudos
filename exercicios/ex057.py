sexo = str(input('Digite o seu sexo [M/F]: ')).strip()[0]
while sexo not in 'MmFf':
    print('Tente novamente\n')
    sexo = str(input('Digite o seu sexo [M/F]: ')).strip()[0]
print('Sexo ‘{}‘ registrado.'.format(sexo))
print('Encerrando...')