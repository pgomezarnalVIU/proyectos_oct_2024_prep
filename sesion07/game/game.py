#Importamos pygame
import pygame
from pacogame import GameObject

#Pygame setup
#Pygame inicializacion
pygame.init()
#Variables del tamaño de nuestra ventana
width=640
height=480
#Surface es el espacio de representacion
screen = pygame.display.set_mode((width,height))

#Cargar el hero
player=GameObject("player",width/2,height/2)

#El juego se ejecute de forma infinita
running = True

#PACOs GAME
while running:
    # pygame.event PILA DE EVENTOS que ocurren en la ventana
    # get -> Dame el primer evento ocurrido
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.unicode == "w":
                print("Subir player")
            if event.unicode == "d":
                print("Derecha player")
            if event.unicode == "a":
                print("Izquierda player")
            if event.unicode == "s":
                print("Bajar player")
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill([188,170,164])
    #Pintamos el hero
    screen.blit(player.get_image(),player.get_rect())
    # RENDER YOUR GAME HERE
    pygame.display.flip()

pygame.quit()