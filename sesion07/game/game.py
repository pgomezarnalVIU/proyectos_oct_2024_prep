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
# Control del movimiento con tecla apretada
key_press=""
player_move=False
# Control del movimiento con tecla apretada
# Control del FLIP de la imagen
player_moving_left=False
player_moving_right=True
# Control del FLIP de la imagen


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
                key_press = "w"
                player_move = True
            elif event.unicode == "d":
                #Control del FLIP de la imagen
                player_moving_right = True
                if player_moving_left:
                    imgFlip=pygame.transform.flip(player.get_image(),True,False)
                    player_moving_left = False
                    player.set_image(imgFlip)
                # Control del FLIP de la imagen
                player.move_right()
                key_press = "d"
                player_move = True
            elif event.unicode == "a":
                # Control del FLIP de la imagen
                player_moving_left = True
                if player_moving_right:
                    imgFlip=pygame.transform.flip(player.get_image(),True,False)
                    player_moving_right = False
                    player.set_image(imgFlip)
                # Control del FLIP de la imagen
                player.move_left()
                key_press = "a"
                player_move = True
            elif event.unicode == "s":
                player.move_down()
                key_press = "s"
                player_move = True
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            #print("Tecla soltada")
            player_move = False

    #El código pasa por aquí como si no hubiera un mañana
    if player_move:
        if key_press == "w":
            player.move_up(2)
        elif key_press == "d":
            player.move_right(2)
        elif key_press == "a":
            player.move_left(2)
        elif key_press == "s":
            player.move_down(2)
    # fill the screen with a color to wipe away anything from last frame
    screen.fill([188,170,164])
    #Pintamos el hero
    screen.blit(player.get_image(),player.get_rect())
    # RENDER YOUR GAME HERE
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()