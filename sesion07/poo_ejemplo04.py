# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Definición de la clase Estudiante que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, nota):
        super().__init__(nombre, edad)
        self.nota = nota

    def mostrar_informacion_estudiante(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Nota: {self.nota}")

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Nota: {self.nota}")

# Crear una instancia de Estudiante
estudiante = Estudiante("Luis", 20, "8.7")
estudiante.mostrar_informacion()   # imprime 'Nombre: Luis, Edad: 20'
#print(estudiante.nota)
estudiante.mostrar_informacion_estudiante()
