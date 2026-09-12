c = 1
MaiorIdade = Homens = MulherMenos20 = 0
while True:
    print('-=-' * 15)
    print(f'Qual o sexo da {c}ª pessoa? ')
    print('\n\033[1;36m[M]\033[m - Masculino\n\033[1;31m[F]\033[m - Feminino')
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).upper().strip()[0]
    idade = int(input(f'\nDigite a idade da {c}ª pessoa: '))
    if idade >= 18:
        MaiorIdade += 1
    if sexo == 'M':
        Homens += 1
    if sexo == 'F' and idade < 20:
        MulherMenos20 += 1
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if esc in 'N':
        break
    c += 1
print('-=-' * 15)
print('\033[1;33mDADOS COLETADOS\033[m')
print(f'Total de pessoas com mais de 18 anos: \033[1;34m{MaiorIdade}\033[m')
print(f'Quantidade de homens cadastrados: \033[1;37m{Homens}\033[m')
print(f'Total de mulheres com menos de 20 anos: \033[1;31m{MulherMenos20}\033[m')
