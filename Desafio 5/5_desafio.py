import pandas
import pyarrow

#Abrimos el archivo sales.parquet
sales_tabla = pandas.read_parquet('Desafio_Nubimetrics\Desafio 5\Dependencias\sales.parquet', engine='pyarrow')
#Abrimos el archivo currenciesClean.csv
currencies_tabla = pandas.read_csv("Desafio_Nubimetrics\Desafio 5\Dependencias\currenciesClean.csv", "r", delimiter = ",")

#Renombramos las columnas para hacer el merge 
currencies_tabla.rename(columns = {'currencyID' : 'currency_id', 'datetrack' : 'date'}, inplace = True)

#Tomamos las columnas que nos interesa 
currencies_tabla_sub = currencies_tabla[['currency_id', 'dolarToLocal']]


#Unimos los dataframes en el campo 'currency_id'
Sales_tabla_full = pandas.merge(sales_tabla ,currencies_tabla_sub, on= 'currency_id', how='left')


#Sales_tabla_full.to_parquet('Sales_DF.parquet')

#Creamos la columna row_key con date + category_id
Sales_tabla_full['row_key'] = Sales_tabla_full['date'] + '-' + Sales_tabla_full['category_id']

#Seleccionamos las columnas que nos interesan
Sales_tabla_full_sub = Sales_tabla_full[['row_key', 'item_id', 'title', 'sales']]
print(Sales_tabla_full_sub)