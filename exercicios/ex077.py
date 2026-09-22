palavras = ('Gulosinho', 'Programar', 'Preguiça',
            'Quase', 'Sempre', 'Mouse', 'Teclado',
            'Chupetinha')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos: ', end = '')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
            