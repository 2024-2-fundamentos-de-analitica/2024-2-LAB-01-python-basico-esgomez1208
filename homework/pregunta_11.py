"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


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
            #Obtener la segunda columna de la linea
            columna2 = int(elements[1])
            #Obtener la cuarta columna de la linea
            columna4 = elements[3]
            #Iterar sobre las letras de la cuarta columna
            for letra in columna4.split(','):
                #Sumar la columna2 a la letra en el diccionario
                diccionario[letra] = diccionario.get(letra, 0) + columna2
    return diccionario
