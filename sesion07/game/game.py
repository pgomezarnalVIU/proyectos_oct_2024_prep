#Importamos pygame
import pygame

#Pygame setup
#Pygame inicializacion
pygame.init()
#Variables del tamaño de nuestra ventana
width=640
height=480
#Surface es el espacio de representacion
screen = pygame.display.set_mode((width,height))
#El juego se ejecute de forma infinita
running = True

while running:
    # pygame.event PILA DE EVENTOS que ocurren en la ventana
    # get -> Dame el primer evento ocurrido
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(event.unicode)
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill([188,170,164])

    # RENDER YOUR GAME HERE
    pygame.display.flip()

pygame.quit()