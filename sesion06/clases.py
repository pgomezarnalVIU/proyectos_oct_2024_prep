#Ejemplos sobre clases

#Clase Perro
#Tiene 2 atributos
# - nombre , str
# - raza , str
class Perro:
    # El método __init__ es llamado al crear el objeto
    def __init__(self, nombreIntroducido, raza):
        print(f"Creando perro {nombre}, {raza}")

        # Atributos de la instancia
        self.nombre = nombreIntroducido
        self.raza = raza


#Generacion de objetos
caniche = Perro("Zeus","caniche")
pastorAleman = Perro("Odin","pastor aleman")
chiuaua = Perro("Loki","chiuaua")