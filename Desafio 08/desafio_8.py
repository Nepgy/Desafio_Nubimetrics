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
print(generarPathUltimosDias(2021105,10))