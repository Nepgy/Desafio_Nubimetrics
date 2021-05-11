import pandas
import pyarrow

#Abrimos el archivo sales.parquet
sales_tabla = pandas.read_parquet('Desafio_Nubimetrics\Desafio 4\Dependencias\sales.parquet', engine='pyarrow')
#Abrimos el archivo currenciesClean.csv
currencies_tabla = pandas.read_csv("Desafio_Nubimetrics\Desafio 4\Dependencias\currenciesClean.csv", "r", delimiter = ",")

#Renombramos las columnas para hacer el merge 
currencies_tabla.rename(columns = {'currencyID' : 'currency_id', 'datetrack' : 'date'}, inplace = True)

#Tomamos las columnas que nos interesa 
currencies_tabla_sub = currencies_tabla[['currency_id', 'dolarToLocal']]


#Unimos los dataframes en el campo 'currency_id'
Sales_tabla_full = pandas.merge(sales_tabla ,currencies_tabla_sub, on= 'currency_id', how='left')

#Cantidad de elementos en el campo item_id
#Cant_items = Sales_tabla_full.item_id.count()
#print(Cant_items)

#Item más vendido
#max_ventas = Sales_tabla_full[Sales_tabla_full.sales == Sales_tabla_full['sales'].max()]
#print(max_ventas.item_id)

Sales_tabla_full.to_parquet('Sales_DF.parquet')	