import pandas
import pyarrow

#Abrimos el archivo sales.parquet
sales_df = pandas.read_parquet('Desafio 06\Dependencias\sales.parquet', engine='pyarrow')
#Abrimos el archivo currenciesClean.csv
currencies_df = pandas.read_csv("Desafio 06\Dependencias\currenciesClean.csv", "r", delimiter = ",")

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

print(df_sales_nivel_ordenado)