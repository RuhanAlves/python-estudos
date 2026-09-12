from datetime import date
MaiorIdade = 0
MenorIdade = 0
AnoAtual = date.today().year
for x in range(1, 8):
    data = int(input('Digite a data de nascimento da {}º pessoa: '.format(x)))
    Test = AnoAtual - data
    if Test >= 21:
        MaiorIdade += 1
    else:
        MenorIdade += 1
print('\nExiste(m) \033[1;34m{}\033[m pessoa(s) maior(es) de idade.'.format(MaiorIdade))
print('E existe(m) \033[1;36m{}\033[m pessoa(s) menor(es) de idade.'.format(MenorIdade))