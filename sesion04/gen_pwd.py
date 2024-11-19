import string
import random


#Funcion genera
# password
def gen_pawd(length,listaCaracteres,pwd):
    #Recorrer el listado de caracteres
    for i in range(length):
        #Elijo un elemento de forma aleatoria
        carac=random.choice(listaCaracteres)
        #Anyado el elemento
        #pwd=""
        #pw+=carac
        pwd.append(carac)

# password
def gen_pawd_str(length,listaCaracteres):
    pwd=""
    #Recorrer el listado de caracteres
    for i in range(length):
        #Elijo un elemento de forma aleatoria
        carac=random.choice(listaCaracteres)
        #Anyado el elemento
        pwd+=carac
    return pwd

#Longitud de un pwd
length = int(input("Introduce la longitud del pwd: "))

#Elementos que utilizaremos para construir el pwd
print("Elige entre los siguientes subgrupos: ")
print(" 1.- Digitos ")
print(" 2.- Minusculas ")
print(" 3.- Mayusculas ")
print(" 4.- Carac especiales ")
print(" 0.- FIN ")

listaCaracteres = ""

#Bucle donde se solicita los elementos
while True:
    opcion = int(input("Elige subconjunto: "))

    if(opcion==1):
        #Anyadir digitos
        listaCaracteres += string.digits
    elif(opcion==2):
        #Anyadir lowercase
        listaCaracteres += string.ascii_lowercase
    elif(opcion==3):
        #Anyadir upercase
        listaCaracteres += string.ascii_uppercase
    elif(opcion==4):
        #Anyadir especiales
        listaCaracteres += string.punctuation
    elif(opcion==0):
        break
    else:
        print("Selecciona una opcion valida")

#Tengo una lista
password =[]
#Genero el pwd
gen_pawd(length,listaCaracteres,password)
#Imprimir el passwd
print(f"El pwd generado es: {password}")
#Imprimir el passwdStr
print(f"El pwd generado es: {gen_pawd_str(length,listaCaracteres)}")
