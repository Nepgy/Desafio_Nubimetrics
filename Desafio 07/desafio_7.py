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
print(generarPathMensuales(2021,11,10))