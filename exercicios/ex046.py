from time import sleep
print('Contagem regressiva: ')
for x in range (10, -1, -1):
    print('\033[33m{}\033[m'.format(x))
    sleep(1)
print('\033[1;35mBOOOM!\033[m 🎆🎇🎇✨')