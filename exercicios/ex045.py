#じょけんぽ -> Jokenpo
from random import choice
from time import sleep
escolha = ['PEDRA', 'PAPEL', 'TESOURA']
comp = choice(escolha)
user = str(input('Pedra, Papel ou Tesoura? ')).upper().strip()
if user not in escolha:
    print('\033[33mEscolha uma opção válida\033[m')
    exit()
print('\033[31mじゃん\033[m')
sleep(1)
print('\033[31mけん\033[m')
sleep(1)
print('\033[31mぽん!\033[m')
if comp == user:
    print('\033[1;33mEmpate!\033[m Você e o computador escolheram {}'.format(comp))
elif (comp == 'PEDRA' and user == 'TESOURA') or \
    (comp == 'PAPEL' and user == 'PEDRA') or \
    (comp == 'TESOURA' and user == 'PAPEL'):
    print('\033[1;34mO computador Venceu!\033[m Ele escolheu {} e você escolheu {}'.format(comp, user))
else:
    print('\033[1;32mVocê Venceu!\033[m O computador escolheu {} e você escolheu {}'.format(comp, user))
