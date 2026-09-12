#Exercicio para verificar se um ano é bissexto ou não
from datetime import date
ano = int(input('Digite um ano: (Digite 0 para analisar o ano atual) '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano \033[33m{}\033[m \033[32mé\033[m um ano bissexto'.format(ano))
else:
    print('O ano \033[33m{}\033[m \033[35mnão\033[m é um ano bissexto'.format(ano))