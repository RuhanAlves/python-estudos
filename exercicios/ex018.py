from math import radians, cos, sin, tan
ang = float(input('Digite o valor do angulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print ('O ângulo de \033[33m{}º\033[m tem \nSeno: \033[36m{:.2f}\033[m'.format(ang, sen))
print ('Cosseno: \033[36m{:.2f}\033[m \nTangente: \033[36m{:.2f}\033[m'.format(cos, tan))