"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

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
            if columna1 not in letras[columna0]:
                letras[columna0].append(columna1)
    #Inicializar la lista de tuplas
    result = []
    #Iterar sobre las claves
    for clave in letras:
        #Agregar la tupla a la lista de resultados
        result.append((clave, sorted(letras[clave])))
    return sorted(result)
