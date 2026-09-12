#Exercicio para analisar de 3 segmentos de retas conseguem formar um triângulo
r1 = float(input('Digite o comprimento do primeiro segmento: '))
r2 = float(input('Digite o comprimento do segundo segmento: '))
r3 = float(input('Digite o comprimento do terceiro segmento: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('\n\033[1;32mÉ possível\033[m formar um triângulo com os valores \033[33m{}, {}\033[m e \033[33m{}\033[m'.format(r1, r2 ,r3))
else:
    print('\n\033[1;35mNão é possível\033[m formar um triângulo com os valores \033[33m{}, {}\033[m e \033[33m{}\033[m'.format(r1, r2, r3))
