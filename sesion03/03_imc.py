print("---- CÁLCULO IMC ----")
print("Introduce tu peso en Kg")
peso = input()
#Ojo con las ,
pesoNum= float(peso)
#Ojo que es un str
#print(type(peso))
print("Introduce tu altura en m")
altura = input()
alturaNum= float(altura)
imc=pesoNum/(alturaNum*alturaNum)
print(f"Tu IMC es {imc:.2f}")




