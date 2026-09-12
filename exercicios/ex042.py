#Exercicio para identificar se há possibilidade de se construir um triângulo e
#qual o tipo de triângulo que será formado pelos segmentos de reta.
r1 = int(input('Digite o valor do primeiro segmento de reta: '))
r2 = int(input('Digite o valor do segundo segmento de reta: '))
r3 = int(input('Digite o valor do terceiro segmento de reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 == r3:
        print('O triângulo com os valores {}, {} e {} é um triângulo \033[1;36mequilátero.\033[m'.format(r1, r2, r3))
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo com os valores {}, {} e {} é um triângulo \033[1;33misósceles.\033[m'.format(r1, r2, r3))
    else:
        print('O triângulo com os valores {}, {} e {} é um triângulo \033[1;32mescaleno.\033[m'.format(r1, r2, r3))
else:
    print('Com os valores {}, {} e {} \033[1;35mNÃO\033[m é possível formar um triângulo.'.format(r1, r2, r3))