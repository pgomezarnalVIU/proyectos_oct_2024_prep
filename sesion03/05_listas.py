#Creacion
mi_lista = [1, 2, 3, 4, 5]
mi_lista_nombre = [ "Monica" , "Carlos", "Paco", "Pablo"]
lista_vacia = []

#Imprimir una lista
for nombre in mi_lista_nombre:
    print(nombre)

#Acceder a un elemento
print(f"El primer nombre es {mi_lista_nombre[0]}")

#Añadir un elemento
mi_lista_nombre.append("Alberto")

#Imprimir una lista
for nombre in mi_lista_nombre:
    print(nombre)

print("------")
#Eliminar "Paco"
#mi_lista_nombre.remove("Paco")
indice=0
for nombre in mi_lista_nombre:
    if(nombre=="Paco"):
        mi_lista_nombre.pop(indice)
    indice=indice+1

#Imprimir una lista
for nombre in mi_lista_nombre:
    print(nombre)