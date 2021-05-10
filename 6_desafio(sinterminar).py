import pandas
import pyarrow

#Abrimos el archivo sales.parquet
sales_tabla = pandas.read_parquet('sales.parquet', engine='pyarrow')
#Abrimos el archivo currenciesClean.csv
currencies_tabla = pandas.read_csv("currenciesClean.csv", "r", delimiter = ",")

#Renombramos las columnas para hacer el merge 
currencies_tabla.rename(columns = {'currencyID' : 'currency_id', 'datetrack' : 'date'}, inplace = True)

#Tomamos las columnas que nos interesa 
currencies_tabla_sub = currencies_tabla[['currency_id', 'dolarToLocal']]

#Unimos los dataframes en el campo 'currency_id'
Sales_tabla_full = pandas.merge(sales_tabla ,currencies_tabla_sub, on= 'currency_id', how='left')

Sales_tabla_full['row_key'] = Sales_tabla_full['date'] + '-' + Sales_tabla_full['category_id']
Sales_tabla_full_sub = Sales_tabla_full[['row_key', 'item_id', 'title', 'sales']]

Sales_tabla_level = Sales_tabla_full[['sales', 'level1', 'level2', 'level3', 'level4', 'level5', 'level6', 'level7']]


#level_tabla = Sales_tabla_level.pivot(columns = ['level1', 'level2', 'level3', 'level4', 'level5', 'level6', 'level7'])
#level_tabla = Sales_tabla_level.unstack().drop_duplicates()

#level_tabla['sum'] = Sales_tabla_level[list(Sales_tabla_level.columns)].sum(axis=1)
#print(level_tabla)

#Level, sales, level_id
#Indice, sum sales, level