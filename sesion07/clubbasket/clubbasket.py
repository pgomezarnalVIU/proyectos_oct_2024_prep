# LIBRERIA PARA LA GESTION DE UN CLUB DE BASKET

#CLASE JUGADOR
# Atributos
#   - nombre[str]
#   - edad[int]
#   - altura[int] (cm)
#   - peso[int] (kg)
#   - dorsal[int]
# Metodos
#   - print_jugador
class Jugador():
    #Constructor
    def __init__(self, nombre="", edad=18, altura=180, peso=75, dorsal=0):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.dorsal = dorsal

    #Imprimir jugador
    def print_jugador(self):
        print(f"Nombre: {self.nombre}, altura: {self.altura}, peso: {self.peso}, edad: {self.edad}, dorsal: {self.dorsal},")