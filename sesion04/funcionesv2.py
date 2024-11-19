def saludar(nombre="Noelia"):
    print("Hola,", nombre)

def saludar_completo(nombre,apellido="Gomez"):
    print("Hola, ", nombre,apellido)

def resta(a,b):
    print(a-b)

# Llamada a la función sin proporcionar un valor para el parámetro
saludar()  # Salida: Hola, Mundo

# Llamada a la función con un valor para el parámetro
saludar("Luis")  # Salida: Hola, Luis

saludar_completo("Paco")
saludar_completo("Paco","Arnal")

#usamos resta
resta(b=4,a=1)


