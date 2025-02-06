"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

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
            #Obtener la columna 0
            columna0 = int(elements[1])
            #Obtener la columna 1
            columna1 = elements[0]
            #Si la columna 0 no esta en el diccionario
            if columna0 not in letras:
                #Agregar la columna 0 al diccionario
                letras[columna0] = []
            #Agregar la columna 1 a la lista de la columna 0
            letras[columna0].append(columna1)
    #Inicializar la lista de tuplas
    result = []
    #Iterar sobre las claves
    for clave in letras:
        #Agregar la tupla a la lista de resultados
        result.append((clave, letras[clave]))
    return sorted(result)
