#Exercicio para calcular uma média de nota na escola e dizer como o aluno se posiciona
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A média do aluno foi: {:.1f}'.format(media))
if media < 5:
    print('Aluno \033[1;35mREPROVADO\033[m')
elif media >= 5 and media <= 6.9:
    print('Aluno em \033[1;33mRECUPERAÇÃO\033[m')
elif media >= 7 and media <= 9.9:
    print('Aluno \033[1;32mAPROVADO\033[m')
else:
    print('\033[1;34mPARABÉNS!!\033[m \033[34mVocê tirou média maxima!\033[m')