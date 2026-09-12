#Exercicio para analisar qual dos números é o maior e qual é o menor
n1 = int(input('Digite um número qualquer: '))
n2 = int(input('Digite um outro número qualquer: '))
n3 = int(input('Digite outro número qualquer: '))
#Verificando número maior
maior = n1
if n2 > maior and n2 > n3:
    maior = n2
elif n3 > maior and n3 > n2:
    maior = n3
#Verificando númerio menor
menor = n1
if n2 < menor and n2 < n3:
    menor = n2
elif n3 < menor and n3 < n2:
    menor = n3
print('O menor número é o \033[32m{}\033[m'.format(menor))
print('O maior número é o \033[31m{}\033[m'.format(maior))