frase = str(input('Digite uma frase: '))
'''letra = frase.split'''
afrase = frase.upper().split()
afrase = ''.join(afrase)
inverso = afrase[::-1]
'''for letra in range(len(afrase) -1, -1, -1):
    inverso += afrase[letra]'''
print('frase escrita ao contrário: \033[33m{}\033[m'.format(inverso))
if afrase == inverso:
    print('A frase: ‘‘{}‘‘ \033[1;32mÉ\033[m um palíndromo'.format(frase))
else:
    print('A frase: ‘‘{}‘‘ \033[1;35mNÃO\033[m é um palíndromo'.format(frase))
#Voltar aqui depois e tentar denovo