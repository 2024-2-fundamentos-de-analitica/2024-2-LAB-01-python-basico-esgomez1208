"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    with open('./files/input/data.csv') as f:
        #Leer las lineas del archivo
        lines = f.readlines()
        #Inicializar la lista de tuplas
        lista = []
        #Iterar sobre las lineas
        for line in lines:
            #Separar los elementos de la linea
            elements = line.strip().split('\t')
            #Obtener la primera columna de la linea
            columna1 = elements[0]
            #Obtener la cuarta columna de la linea
            columna4 = elements[3]
            #Obtener la quinta columna de la linea
            columna5 = elements[4]
            #Agregar la tupla a la lista
            lista.append((columna1, len(columna4.split(',')), len(columna5.split(','))))
    return lista
