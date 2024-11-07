#Range
lista_5_numeros = range(5)

# Ejemplo de bucle for con range(5)
for i in lista_5_numeros:
    print(i)

print("------")
# Ejemplo de bucle for con range(1,5)
for i in range(1,5,1):
    print(i)
print("------")
# Ejemplo de bucle for con range(1,5)
for i in range(1,6,1):
    print(i)

print("----100 primeros pares--")
#Calculo de la suma de los 100 primeros pares
suma=0
for i in range(2,100,2):
    suma=suma+i # suma += i
    #print(i)
print(suma)