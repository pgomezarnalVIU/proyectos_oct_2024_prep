class Animal:
    #Constructor
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

        #Atributo privado
        self.__marca_padre = "X"

    # Método genérico
    def hablar(self):
        print("No se como hablo")

    # Método genérico
    def moverse(self):
        # Método vacío
        pass

    # Método genérico
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)

# Perro hereda de Animal
#class Perro(Animal):
#    pass

#Clase Perro que hereda de Animal
class Perro(Animal):
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")

#Clase Perro que hereda de Animal
class Gato(Animal):
    def moverse(self):
        print("Caminando con 4 patas")

#Clase Vaca que hereda de Animal
class Vaca(Animal):
    def hablar(self):
        print("Muuu!")
    def moverse(self):
        print("Caminando con 4 patas")

#Clase Abeja que hereda de Animal
class Abeja(Animal):
    def hablar(self):
        print("Bzzzz!")
    def moverse(self):
        print("Volando")

    # Nuevo método
    def picar(self):
        print("Picar!")


#Uso de las clases
animal = Animal ("mamifero",120)
animal.describeme()

perro = Perro("mamifero",2)
perro.describeme()
perro.hablar()

gato = Gato("mamifero",1)
gato.describeme()
gato.hablar()

abeja = Abeja("insecto",1)
abeja.picar()