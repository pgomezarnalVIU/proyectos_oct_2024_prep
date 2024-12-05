import pygame

#Clase GameObject
#   Atributos
#   - tag
#   - pos_x
#   - pos_y
#   - image
#
#   Metodo
#   - get_image: Devuelve una image de pygame para ese gameobject
#   - get_rect: Devuelve el rectangulo que ocupa este gameobject
class GameObject:

    #constructor
    def __init__(self,tag,pos_x=0,pos_y=0,image="fallenangel.png"):
        print(f"Creando el GameObject {tag}")

        #Atributos de la instancia
        self.tag = tag
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = image

        #Atributos privados
        self.__img = pygame.image.load(self.image)
        self.__img.convert()
        self.__rect = self.__img.get_rect()
        self.__rect.center = pos_x, pos_y

    #Mover hacia arriba el gameobject
    def move_up(self,y=5):
        self.__rect.move_ip(0,-y)

    #Mover hacia derecha el gameobject
    def move_right(self,x=5):
        self.__rect.move_ip(x,0)

    #Mover hacia izquierda el gameobject
    def move_left(self,x=5):
        self.__rect.move_ip(-x,0)

    #Mover hacia abajo el gameobject
    def move_down(self,y=5):
        self.__rect.move_ip(0,y)

    #Funcion que devuelve la imagen del game_object
    def get_image(self):
        return self.__img

    #Funcion que devuelve la imagen del game_object
    def get_rect(self):
        return self.__rect