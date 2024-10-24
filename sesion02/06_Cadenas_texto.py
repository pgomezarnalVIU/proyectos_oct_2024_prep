# Print

print("Hola Pakito")

# Diferentes definiciones

cadena_simple = 'Hola, mundo!'
cadena_doble = "¡Hola, mundo!"
cadena_triple = """Este es un ejemplo
de una cadena con múltiples líneas."""

print(cadena_triple)

# Concatenacion

saludo = "Hello"
nombre = "Pakito"

print(saludo+" "+nombre)

# Formateo v1
nombre = "Juan"
edad = 30
mensaje = "Hola, mi nombre es {} y tengo {} años.".format(nombre,edad)
print(mensaje)  # Salida: "Hola, mi nombre es Juan y tengo 30 años."

# F-string (Python 3.6+)
mensaje_fstring = f"Hola, mi nombre es {nombre} y tengo {edad} años."
# print(mensaje_fstring)  # Salida: "Hola, mi nombre es Juan y tengo 30 años."
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")





