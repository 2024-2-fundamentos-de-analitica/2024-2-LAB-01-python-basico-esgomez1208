"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    with open('./files/input/data.csv') as f:
        #Leer las lineas del archivo
        lines = f.readlines()
        #Inicializar el diccionario de letras
        letras = {}
        #Iterar sobre las lineas
        for line in lines:
            #Separar los elementos de la linea
            elements = line.strip().split('\t')
            #Obtener la quinta columna de la linea
            columna = elements[4]
            #Iterar sobre la columna
            #Obtener la clave
            colsplit = columna.split(',')
            print(colsplit)
            for j in range (len (colsplit)):
                clave, valor = colsplit[j].split(':')
                valor = int(valor)
                #Si la clave no esta en el diccionario
                if clave not in letras:
                    #Agregar la clave al diccionario
                    letras[clave] = 0
                #Agregar el valor a la lista de la clave
                letras[clave] += 1
    #Inicializar la lista de tuplas
    print(sorted(letras))
    return letras
