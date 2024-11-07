#Creacion de diccionarios
registro_sara = {
  "Nombre": "Sara",
  "Edad": 27,
  "Documento": 1003882
}
registro_paco = dict([
      ('Nombre', 'Paco'),
      ('Edad', 49),
      ('Documento', 454678456),
])
print(registro_paco)
#Acceder a elemento
print(registro_paco["Nombre"])
#Cambio de documento
registro_paco["Documento"]=64
print(registro_paco)

#Imprimir todos los elementos de un diccionario
# Imprime las claves del diccionario
for clave in registro_paco:
    print(clave)

# Imprime las claves del diccionario
for clave in registro_paco:
    print(registro_paco[clave])

#Imprime todo
for clave,valor in registro_paco.items(): # ("Nombre","Paco") ("Edad",49)
    print(f"{clave} - {valor}")


