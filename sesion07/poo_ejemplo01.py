class Persona:
    def __init__(self, nombre, edad, edadsucia):
        self.__nombre = nombre
        self.__edad = edad
        self.edadSucia = edadsucia

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena de texto")

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if isinstance(edad, int) and edad > 0:
            self.__edad = edad
        else:
            #raise ValueError("La edad debe ser un número entero positivo")
            print("La edad debe ser un número entero positivo")


#Uso de getter & setter sobre Persona
paco = Persona ("Paco",49,49)
print(paco.get_edad())
paco.edadSucia = -2
paco.set_edad(-2)
print(paco.get_edad())
print(paco.edadSucia)
paco.set_nombre(45)