"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open('./files/input/data.csv') as f:
        #Leer las lineas del archivo
        lines = f.readlines()
        #Inicializar el diccionario
        diccionario = {}
        #Iterar sobre las lineas
        for line in lines:
            #Separar los elementos de la linea
            elements = line.strip().split('\t')
            #Obtener la primera columna de la linea
            columna1 = elements[0]
            #Obtener la quinta columna de la linea
            columna5 = elements[4]
            #Sumar la columna5 a la columna1 en el diccionario
            par = columna5.split(',')
            print(par)
            for i in par:
                val = int(i[4:])
                print(val)
                diccionario[columna1] = diccionario.get(columna1, 0) + val
    print(diccionario)
    return diccionario
