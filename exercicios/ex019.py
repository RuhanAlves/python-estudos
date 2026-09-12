from random import choice
a1 = input('Digite o nome do 1º aluno: ')
a2 = input('Digite o nome do 2º aluno: ')
a3 = input('Digite o nome do 3º aluno: ')
a4 = input('Digite o nome do 4º aluno: ')

aleatorio = [a1, a2, a3, a4]
quem = choice(aleatorio)

print('\nO aluno que vai ter apagar o quadro é o: \033[34m{}'.format(quem))

