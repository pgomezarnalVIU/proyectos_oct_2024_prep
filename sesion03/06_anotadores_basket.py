#Lista creada
lista_anotaciones =[]
lista_jugadores =[]
maxima_anotacion = 0
nombre_jugador_maxima_anotacion = ""
for jugador in range(3):
    #Solicitar las anotaciones
    jugador = input(f"Introduce el nonbre del jugador {jugador}")
    anotacion=int(input(f"Introduce la anotacion del jugador {jugador}"))
    #Anyadir a una lista
    lista_jugadores.append(jugador)
    lista_anotaciones.append(anotacion)
    #El maximo anotador
    if(anotacion>maxima_anotacion):
        maxima_anotacion = anotacion
        nombre_jugador_maxima_anotacion = jugador

#Imprimimos
for i in range(3):
    print(f"Jugador {lista_jugadores[i]} - Anotacion [{lista_anotaciones[i]}]")

print(f"Maximo anotador es {nombre_jugador_maxima_anotacion} con {maxima_anotacion} ptos")
