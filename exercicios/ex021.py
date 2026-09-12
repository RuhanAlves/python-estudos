import pygame
pygame.init()
pygame.mixer.music.load('Roommates.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('\033[41mAperte ENTER para parar a musica: ')
pygame.quit()

