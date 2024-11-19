#Suma
def suma(a,b):
    return a+b
#Resta
def resta(a,b):
    return a-b
#Multiplicacion
def mult(a,b,pa=1,pb=1):
    return a*b
#Division
def division(a,b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    return result

#Interfaz de usuario
print("Seleccionar la operacion")
print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")
print("4.Dividir")
print("----------")
print("0.Salir")

#Bucle Infinito
while True:
    #pedir opcion
    opcion = input("Introduce opcion[1,2,3,4,0]")

    if opcion in ('0','1','2','3','4'):
        #Operaciones
        if opcion == '0':
            break
        #Capturamos dos numeros
        try:
            num1 = float(input("Introduce el primer numero: "))
            num2 = float(input("Introduce el segundo numero: "))
        except ValueError:
            print("Porfa introduce dos numeros válidos")
            continue

        if opcion == '1':
            print(f"La suma es: {suma(num1,num2)}")
        elif opcion == '2':
            print(f"La resta es: {resta(num1,num2)}")
        elif opcion == '3':
            print(f"La multiplicacion es: {mult(num1,num2)}")
        elif opcion == '4':
            try:
                print(f"La division es: {division(num1,num2)}")
            except ZeroDivisionError:
                print("Division por 0")
                continue
    else:
        print("Introduce una opcion valida")

#FIN Bucle
print("Gracias por usar mi app")