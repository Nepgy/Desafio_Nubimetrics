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

def desafio_2():
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

def pathFolder():
    return carpeta_correspondiente
def pathJson():
    return carpeta_correspondiente + "\\" + "MLA1055.json"
#####################################################################

import pandas
import csv

def desafio_3():
    #Tomar el archivo y pasarlo a un CSV para facilitar el analisis
    with open('Desafio 03\Dependencias\currenciesRaw', 'r') as en_file:
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

#####################################################################

import pandas
import pyarrow

def desafio_4():
    #Abrimos el archivo sales.parquet
    sales_df = pandas.read_parquet('Desafio 04\Dependencias\sales.parquet', engine='pyarrow')
    #Abrimos el archivo currenciesClean.csv
    currencies_df = pandas.read_csv("Desafio 04\Dependencias\currenciesClean.csv", "r", delimiter = ",")

    #Renombramos las columnas para hacer el merge 
    currencies_df.rename(columns = {'currencyID' : 'currency_id', 'datetrack' : 'date'}, inplace = True)

    #Tomamos las columnas que nos interesa 
    currencies_df_sub = currencies_df[['currency_id', 'dolarToLocal']]


    #Unimos los dataframes en el campo 'currency_id'
    Sales_df_full = pandas.merge(sales_df ,currencies_df_sub, on= 'currency_id', how='left')

    #Cantidad de elementos en el campo item_id
    #Cant_items = Sales_df_full.item_id.count()
    #print(Cant_items)

    #Item más vendido
    #max_ventas = Sales_df_full[Sales_df_full.sales == Sales_df_full['sales'].max()]
    #print(max_ventas.item_id)

    Sales_df_full.to_parquet('Sales_DF.parquet')

#####################################################################

import pandas
import pyarrow


def desafio_5():
    #Abrimos el archivo sales.parquet
    sales_df = pandas.read_parquet('Desafio 04\Dependencias\sales.parquet', engine='pyarrow')
    #Abrimos el archivo currenciesClean.csv
    currencies_df = pandas.read_csv("Desafio 04\Dependencias\currenciesClean.csv", "r", delimiter = ",")

    #Renombramos las columnas para hacer el merge 
    currencies_df.rename(columns = {'currencyID' : 'currency_id', 'datetrack' : 'date'}, inplace = True)

    #Tomamos las columnas que nos interesa 
    currencies_df_sub = currencies_df[['currency_id', 'dolarToLocal']]


    #Unimos los dataframes en el campo 'currency_id'
    Sales_df_full = pandas.merge(sales_df ,currencies_df_sub, on= 'currency_id', how='left')


    #Sales_tabla_full.to_parquet('Sales_DF.parquet')

    #Creamos la columna row_key con date + category_id
    Sales_df_full['row_key'] = Sales_df_full['date'] + '-' + Sales_df_full['category_id']

    #Seleccionamos las columnas que nos interesan
    Sales_df_full_sub = Sales_df_full[['row_key', 'item_id', 'title', 'sales']]
    Sales_df_full_sub.to_parquet('Sales_DF_row_key.parquet')

#####################################################################

import pandas
import pyarrow

def desafio_6():
        
    #Abrimos el archivo sales.parquet
    sales_df = pandas.read_parquet('Desafio 04\Dependencias\sales.parquet', engine='pyarrow')
    #Abrimos el archivo currenciesClean.csv
    currencies_df = pandas.read_csv("Desafio 04\Dependencias\currenciesClean.csv", "r", delimiter = ",")

    #Renombramos las columnas para hacer el merge 
    currencies_df.rename(columns = {'currencyID' : 'currency_id', 'datetrack' : 'date'}, inplace = True)

    #Tomamos las columnas que nos interesa 
    currencies_df_sub = currencies_df[['currency_id', 'dolarToLocal']]

    #Unimos los dataframes en el campo 'currency_id'
    Sales_df_full = pandas.merge(sales_df ,currencies_df_sub, on= 'currency_id', how='left')

    #Creamos la columna row_key con date + category_id
    Sales_df_full['row_key'] = Sales_df_full['date'] + '-' + Sales_df_full['category_id']

    #Seleccionamos las columnas que nos interesan
    Sales_df_full_sub = Sales_df_full[['row_key', 'item_id', 'title', 'sales']]

    #Desafio 6 ----------

    #df con todos los niveles y las ventas
    Sales_df_level = Sales_df_full[['sales', 'level1', 'level2', 'level3', 'level4', 'level5', 'level6', 'level7']]

    #Creamos una lista con los levels
    levels = ['level1', 'level2', 'level3', 'level4', 'level5', 'level6', 'level7']

    #Usamos la funcion melt para transformar los campos en nuetros nuevos valores para relacionar level_id con su level
    df_level = pandas.melt(Sales_df_level, value_vars = levels, var_name = 'level', value_name = 'level_id', ignore_index = True )
    df_level.reset_index(drop = True, inplace = True)

    #Un df auxiliar para relacionar 'sales' con 'level_id'
    Sales_df_aux = Sales_df_full[['category_id', 'sales']]
    df_level_full = df_level.join(Sales_df_aux, on=None, how='left', lsuffix='level_id', rsuffix='category_id', sort=False)

    #Un sub dataframe con los campos de 'level' y 'level_id'
    df_level_id = df_level_full[['level', 'level_id']]

    #Como hay celdas vacias pero no nulas, tenemos que reemplazarlas para eliminarlas
    #luego se hace el drop de los nullos
    #y el ultimo paso reinicia el index
    null_o = float("NaN")
    df_level_id.replace("", null_o, inplace=True)
    df_level_id.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)
    df_level_id.reset_index(drop=True)

    #Acá tenemos la parte derecha del dataframe que buscamos crear
    df_level_right = df_level_id[['level','level_id']].reset_index(drop=True)


    #Comenzamos con la parte izquierda, creando el dataframe
    df_level_left = pandas.DataFrame()

    #Juntamos las sumas de las ventas por su respectivo grupo, creando la parte derecha del dataframe final
    for level in levels:
        sales_sum = sales_df.groupby([level]).sales.sum()
        sales = sales_sum.reset_index()
        sales.columns= ['level_id', 'sales']
        df_level_left = df_level_left.append(sales)

    #El resultado es el merge de la parte izquierda y derecha, que se realiza sobre el level_id
    result = pandas.merge(df_level_left, df_level_right, on="level_id")

    #Sacamos los valores que se repiten
    resultados = result.drop_duplicates()

    #Tomamos los campos que nos interesan y reseteamos el index
    df_final_sales_por_nivel = resultados[['level', 'level_id', 'sales']].reset_index(drop=True)

    #Lo ordenamos de forma descendiente
    df_sales_nivel_ordenado = df_final_sales_por_nivel.sort_values(by = 'sales', ascending = False)

    #print(df_sales_nivel_ordenado)
    df_sales_nivel_ordenado.to_parquet('df_sales_nivel_ordenado.parquet')
    #Ventas por nivel
    ventas_nivel = df_final_sales_por_nivel.groupby('level').sales.sum()
    ventas_nivel_ordenado = ventas_nivel.reset_index()

    #print(ventas_nivel_ordenado)
    ventas_nivel_ordenado.to_parquet('ventas_nivel_ordenado.parquet')

#####################################################################

#Definimos nuestra funcion
#Los parametros los tomamos como INT para poder operar con ellos
def generarPathMensuales(año, mes, dia):
    #Creamos lista Vacia para realizar el .append
    lista_paths = []

    #Hacemos la iteracion para llenar la lista
    for day in range(dia):
        
        #el dia+1 es porque el indice comienza en 0 y no existe realmente el dia 0 del mes
        #Luego hacemos el str() para transformarlos en strings y concatenarlos, creando el path
        lista_paths.append("https://importantdata@location/"+ str(año) +"/"+ str(mes) +"/"+ str(day+1) +"/")

    #La funcion devuelve una lista con todos los path del 1 al dia que se ingresa como parametro
    return lista_paths

#Un ejemplo 
#print(generarPathMensuales(2021,11,10))

#####################################################################

#Definimos nuestra funcion
#Los parametros los tomamos como INT para poder operar con ellos
def generarPathUltimosDias(fecha, dias):
    #Creamos lista Vacia para realizar el .append
    lista_paths = []

    #Tomamos el string Fecha y extraemos por separado dia, mes, año para armar el path
    dia = str(fecha)[-2:]
    mes = str(fecha)[4:6]
    año = str(fecha)[:4]

    #Hacemos la iteracion para llenar la lista
    for day in range(dias):
        
        #Realizamos el dia - n
        dia_calculator = int(dia) - day
        #Lo pasamos a string para la lista
        
        
        #Chequeamos que no sea 0 o menor porque no existe el dia 0
        if dia_calculator <= 0:
            break

        #Lo pasamos a string para la lista
        dia_string = str(dia_calculator)
        
        #Armamos el path y hacemos el .append()   
        lista_paths.append("https://importantdata@location/"+ año +"/"+ mes +"/"+ dia_string +"/")

    #La funcion devuelve una lista con todos los path generados
    return lista_paths

#Un ejemplo 
#print(generarPathUltimosDias(2021105,10))

#####################################################################