import pandas
import pyarrow

#Abrimos el archivo sales.parquet
sales_df = pandas.read_parquet('Desafio_Nubimetrics\Desafio 4\Dependencias\sales.parquet', engine='pyarrow')
#Abrimos el archivo currenciesClean.csv
currencies_df = pandas.read_csv("Desafio_Nubimetrics\Desafio 4\Dependencias\currenciesClean.csv", "r", delimiter = ",")

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