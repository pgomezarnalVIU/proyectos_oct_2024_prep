#Funcion saludo
def saludo():
    print("Hola Paco")

#Funcion suma
def suma(a, b):
    print(a + b)
#Funcion suma
def sumaReturn(a, b):
    return (a + b)
#Funcion suma
def division(a, b):
    print(a / b)

#Usar saludo
saludo()

#Usamos suma
suma(27652, 5) # llamamos a la función

CONSTANTE=20
for i in range(1,5,1):
    suma(CONSTANTE, i)

#Usar sumaReturn
result=sumaReturn(27652, 5)
print(f"El resultado es {result}")