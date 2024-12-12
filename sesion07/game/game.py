#Importamos pygame
import pygame
from pacogame import GameObject

#Pygame setup
#Pygame inicializacion
pygame.init()
#Variables del tamaño de nuestra ventana
width=300
height=300
#Surface es el espacio de representacion
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

#Cargar el hero
player=GameObject("player",screen,width/2,height/2)
playerMove=False
keyPress=""

#El juego se ejecute de forma infinita
running = True

#PACOs GAME
while running:
    # pygame.event PILA DE EVENTOS que ocurren en la ventana
    # get -> Dame el primer evento ocurrido
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #print("Tecla apretada")
            if event.unicode == "w":
                player.move_up()
                keyPress = "w"
                playerMove = True
            elif event.unicode == "d":
                player.move_right()
                keyPress = "d"
                playerMove = True
            elif event.unicode == "a":
                player.move_left()
                keyPress = "a"
                playerMove = True
            elif event.unicode == "s":
                player.move_down()
                keyPress = "s"
                playerMove = True
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            #print("Tecla soltada")
            playerMove = False

    #El código pasa por aquí como si no hubiera un mañana
    if playerMove:
        if keyPress == "w":
            player.move_up(2)
        elif keyPress == "d":
            player.move_right(2)
        elif keyPress == "a":
            player.move_left(2)
        elif keyPress == "s":
            player.move_down(2)
    # fill the screen with a color to wipe away anything from last frame
    screen.fill([188,170,164])
    #Pintamos el hero
    screen.blit(player.get_image(),player.get_rect())
    # RENDER YOUR GAME HERE
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()