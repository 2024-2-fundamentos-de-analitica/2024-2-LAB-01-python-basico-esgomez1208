"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    # Abrir el archivo data.csv
    with open('./files/input/data.csv') as f:
        # Leer las lineas del archivo
        lines = f.readlines()
        # Inicializar el diccionario de letras
        letras = {}
        # Iterar sobre las lineas
        for line in lines:
            # Separar los elementos de la linea
            elements = line.strip().split('\t')
            # Obtener la primera letra de la linea
            letra = elements[0]
            # Obtener el valor de la segunda columna
            valor = int(elements[1])
            # Si la letra no esta en el diccionario
            if letra not in letras:
                # Agregar la letra al diccionario
                letras[letra] = 0
            # Incrementar la cantidad de la letra
            letras[letra] += valor
    # Retornar la lista de tuplas ordenadas
    return sorted(letras.items())
