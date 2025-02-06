"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

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
                letras[letra] = []
            # Agregar el valor a la lista de la letra
            letras[letra].append(valor)
    # Inicializar la lista de tuplas
    result = []
    # Iterar sobre las letras
    for letra in letras:
        # Obtener el maximo y el minimo de la lista
        maximo = max(letras[letra])
        minimo = min(letras[letra])
        # Agregar la tupla a la lista de resultados
        result.append((letra, maximo, minimo))
    # Retornar la lista de tuplas ordenadas
    return sorted(result)
