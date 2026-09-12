#Exercicio para identificar sexo de uma pessoa e informar sobre o alistamento miltiar de um cidadão
from datetime import date
print('''Qual o seu sexo?
(M) para masculino
(F) para femenino''')
sexo = str(input('Sua escolha: ')).strip().upper()
if sexo == 'F':
    print('\033[33mVocê não precisa fazer alistamento militar \033[1;33mobrigatoriamente.\033[m')
    quit()
nascimento = int(input('Informe o ano da data de seu nascimento: '))
idade = date.today().year - nascimento
if idade == 18:
    print('\033[32mJá está na \033[1;32mhora\033[m \033[32mde se alistar ao exército.\033[m')
elif idade < 18:
    print('\033[33mVocê ainda \033[4;33mdeverá\033[m \033[33mse alistar ao exército.\033[m')
    print('Falta ainda \033[32m{} ano(s)\033[m para se alistar.'.format(18 - idade))
    ano = 18 - idade + date.today().year
    print('O seu alistamento será em \033[1;33m{}.\033[m'.format(ano))
else:
    print('\033[35mTempo limite para o alistamente \033[1;35mexcedido.\033[m')
    print('Se passaram \033[1;34m{} ano(s)\033[m do tempo \033[1;35mlimite\033[m para se alisatar.'.format(idade - 18))
    ano = date.today().year - (idade - 18)
    print('O seu alistamento foi em \033[1;33m{}.\033[m'.format(ano))