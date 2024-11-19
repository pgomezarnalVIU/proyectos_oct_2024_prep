# Ejemplo con un tipo básico (int)
def modificar_numero(numero):
    numero = numero * 2

# Ejemplo con una referencia (lista)
def modificar_lista(lista):
    lista.append(4)


numero_original = 5
print("Número original antes de llamar a la función:", numero_original)
modificar_numero(numero_original)
print("Número original después de llamar a la función:", numero_original)


lista_original = [1, 2, 3]
modificar_lista(lista_original)
print("Lista original después de llamar a la función:", lista_original)  # Resultado: [1, 2, 3, 4]
