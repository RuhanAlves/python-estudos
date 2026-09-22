from random import shuffle
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')

ordem = [a1, a2, a3, a4]
shuffle(ordem)

print('\nAlunos em ordem para apresentar:')
print('1º aluno: \033[31m{}\033[m'.format(ordem[0]))
print('2º aluno: \033[32m{}\033[m'.format(ordem[1]))
print('3º aluno: \033[33m{}\033[m'.format(ordem[2]))
print('4º aluno: \033[34m{}\033[m'.format(ordem[3]))
