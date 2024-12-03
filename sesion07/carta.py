from enum import Enum

class Tipo(Enum):
    ELECTRICO = 1
    AIRE = 2
    TIERRA = 3
    AGUA = 4

#Carta
# propiedades
# -nombre
# -tipo
# -defensa
# -ataque
#
# metodo
# -quitarVida
class Carta:

    #constructor
    def __init__(self,nombre,ataque=10,defensa=10,tipo=Tipo.AIRE):
        self.nombre = nombre
        self.ataque = ataque
        self.__defensa = defensa
        self.tipo = tipo
        self.__nombreInterno="SIN DEFINIR"

    def quitarVida(self,ptosDanyo):
        #self.defensa = self.defensa - ptosDanyo
        self.__defensa -=  ptosDanyo
        return self.__defensa

    def printCarta(self):
        print("------------")
        print(f"Nombre: {self.nombre}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.__defensa}")
        print(f"Tipo: {self.tipo}")
        print("------------")

    def printCartaDeveloper(self):
        print("------------")
        print(f"Nombre: {self.nombre}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.__defensa}")
        print(f"Tipo: {self.tipo}")
        print(f"Nombre interno: {self.__nombreInterno}")
        print("------------")
