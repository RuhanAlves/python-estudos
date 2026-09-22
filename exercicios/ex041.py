#Exercicio para calcular idade de um atleta e informá-lo a sua categoria de acordo com a sua idade
from datetime import date
nascimento = int(input('Digite a sua data de nascimento: '))
idade = date.today().year - nascimento
if idade > 0 and idade <= 9:
    print('Categoria \033[1;34mMIRIM')
elif idade <= 14:
    print('Categoria \033[1;31mINFANTIL')
elif idade <= 19:
    print('Categoria \033[1;32mJUNIOR')
elif idade <= 25:
    print('Categoria \033[1;36mSENIOR')
else:
    print('Categoria \033[7mMASTER\033[m')