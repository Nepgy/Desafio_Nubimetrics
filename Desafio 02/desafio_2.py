import requests
import json
import os
import datetime

#Hacemos el request sobre el URL de Mercado Libre
mercadoLibreUrl = "https://api.mercadolibre.com/sites/MLA/search?category=MLA1055"
response = requests.get(mercadoLibreUrl)
datos = response.json()

#Tomamos el .Json file y lo guardamos en su carpeta correspodiente al formato NombreApi+Formato+año+mes+dia
date_ahora = datetime.datetime.now()
nombreApi = "MLA"
formato = "Json"
año = date_ahora.year
mes = date_ahora.month
dia = date_ahora.day

carpeta_correspondiente = nombreApi + formato+ "-" + str(año) + "-" + str(mes) + "-" + str(dia)

#Chequeamos que el directorio no exista, y que nos avisé en el caso de que sí
try:
    os.mkdir(carpeta_correspondiente)
    print(carpeta_correspondiente + " creada con exito")
except FileExistsError:
    print(carpeta_correspondiente + " ya existe")

#Escribimos el .json en la carpeta
archivoJson = open(carpeta_correspondiente + "\\" + "MLA1055.json", "x")
archivoJson.write(str(datos))
archivoJson.close()


