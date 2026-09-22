Cels = int(input('Digite a temperatura em Celsius: '))
Fah = Cels * 1.8 + 32
Kelvin = 273
print('Conversão de Celsius para:\nFahrenheit: \033[35m{:.1f}ºF\033[m '.format(Fah))
print('Kelvin: \033[36m{:.1f}K'.format(Kelvin+Cels))