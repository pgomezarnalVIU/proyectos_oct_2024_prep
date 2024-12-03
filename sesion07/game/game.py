#Importamos pygame
import pygame

#Pygame setup
#Pygame inicializacion
pygame.init()
width=640
height=480
screen = pygame.display.set_mode((width,height))
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(event.unicode)
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill([225,190,231])

    # RENDER YOUR GAME HERE
    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()