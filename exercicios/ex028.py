#Analise de número gerado pelo computador para o usuário tentar acertálo
from random import randint
from time import sleep
n1 = randint(1, 5)
print('\033[34m-=-\033[m' * 17)
descoberta = int(input('Tente descobrir o número que eu pensei de 1 a 5: '))
print('\033[34m-=-\033[m' * 17)
print('\033[33mPROCESSANDO...\033[m')
sleep(2)
if n1 == descoberta:
    print('\033[32mParabéns! você acertou o número!\033[m')
else:
    print('\033[35mVocê errou, eu pensei no número {} e não no {}'.format(n1, descoberta))