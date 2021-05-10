import pandas
import csv

#Tomar el archivo y pasarlo a un CSV para facilitar el analisis
with open('Desafio_Nubimetrics\Desafio 3\Dependencias\currenciesRaw', 'r') as en_file:
    stripped = (linea.strip() for linea in en_file)
    lineas = (linea.split("\t") for linea in stripped if linea)
    with open('log.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Country', 'Datetrack', 'Time','Country2', 'Currency','datetrack2','DollarToLocal','Nothing', 'LocalToDollar', 'nothing2', 'Site'))
        writer.writerows(lineas)

#Lo tomamos al archivo con panda
log = pandas.read_csv("log.csv")

#Agarramos las columnas que necesitamos solamente
columnas_need = ['Datetrack','Country','Currency','Site','DollarToLocal','LocalToDollar']

#Redondeamos los decimales de las columnas
currencies = log[columnas_need].round(2)
#Lo escribimos en un CSV que con los datos ordenados que nos sirven
currencies.to_csv("Currencies.csv", index=False)


