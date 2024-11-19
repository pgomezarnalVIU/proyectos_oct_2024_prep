import pandas as pd

#Importar datos
datos = pd.read_csv("datos.csv")

print(datos.head())
datos_filtrados=datos.loc[20:50]
print(datos_filtrados)
datos_filtrados.to_csv("datos_filtrados.csv")
