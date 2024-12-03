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
    def __init__(self,nombre,ataque,defensa,tipo=Tipo.AIRE):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.tipo = tipo

    def quitarVida(self,ptosDanyo):
        #self.defensa = self.defensa - ptosDanyo
        self.defensa -=  ptosDanyo

    def printCarta(self):
        print(f"Nombre: {self.nombre}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Tipo: {self.tipo}")
