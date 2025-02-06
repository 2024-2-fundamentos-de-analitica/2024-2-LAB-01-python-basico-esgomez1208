"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

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
            # Obtener la quinta columna de la linea
            columna = elements[4]
            # Iterar sobre la columna
            for i in range(0, len(columna)):
                # Obtener la clave
                colsplit = columna.split(',')
                print(colsplit)
                for j in range (len (colsplit)):
                    clave, valor = colsplit[j].split(':')
                    valor = int(valor)
                    # Si la clave no esta en el diccionario
                    if clave not in letras:
                        # Agregar la clave al diccionario
                        letras[clave] = []
                    # Agregar el valor a la lista de la clave
                    letras[clave].append(valor)
    # Inicializar la lista de tuplas
    result = []
    # Iterar sobre las claves
    for clave in letras:
        # Obtener el maximo y el minimo de la lista
        maximo = max(letras[clave])
        minimo = min(letras[clave])
        # Agregar la tupla a la lista de resultados
        result.append((clave, minimo, maximo))
    # Retornar la lista de tuplas ordenadas
    return sorted(result)
