from enum import Enum

#Ejemplo sobre VC

class Vacia:
    pass

class TipoAnimales(Enum):
    MAMIFEROS = 1
    OVIPAROS = 2

#Ejemplos sobre clases

##################################################
# Definiendo la clase Dog
# Clase Dog
# Tiene 2 atributos
# - nombre , str
# - raza , str
class Dog:
    #Atributo de clase
    especie = TipoAnimales.MAMIFEROS
    habla = 'Guau'
    pasosTotales = 0

    # El metodo constructor
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza} de especie {self.especie}")

        # Atributos de la instancia
        self.nombre = nombre
        self.raza = raza

    # Metodo ladrar
    def ladra(self):
        #A fuego en el codigo
        #print("Guau")
        print(self.habla)

    # Metodo camina
    def camina(self,pasos):
        #Debo incrementar los pasos totales
        self.pasosTotales = self.pasosTotales + pasos
        print(f"He caminado {pasos}")

##################################################
#Generacion de objetos
#Instanciando la clase = crear objetos
caniche = Dog("Zeus", "caniche")
pastorAleman = Dog("Odin", "pastor aleman")
chiuaua = Dog("Loki", "chiuaua")

print(f"Nombre del caniche es {caniche.nombre}")
print(f"Raza del chiuaua es {caniche.raza}")
print(f"Especie del pastorAleman es {caniche.especie}")

caniche.ladra()
chiuaua.camina(10)
print(f"El chiuaua ha caminado {chiuaua.pasosTotales}")
chiuaua.camina(5)
print(f"El chiuaua ha caminado {chiuaua.pasosTotales}")