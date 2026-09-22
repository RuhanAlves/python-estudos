MulherMenos21 = 0
Maior = 0
velho = ''
media = 0
for i in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(i))).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i)))
    media += idade
    sexo = str(input('Informe o sexo: (M) ou (F) ')).upper().strip()
    print('')
    if idade > Maior and sexo == 'M':
        Maior = idade
        velho = nome
    if sexo == 'F' and idade < 20:
        MulherMenos21 += 1
print('\nMédia de idade do grupo: {:.1f} Anos'.format(media/4))
print('Nome do homem mais velho: {}'.format(velho))
print('Quantidade de mulheres menores de 21 anos: {}'.format(MulherMenos21))