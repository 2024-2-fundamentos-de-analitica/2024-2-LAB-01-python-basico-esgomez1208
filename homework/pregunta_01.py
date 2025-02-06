"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
        # Abrir y leer el archivo CSV
    with open("files/input/data.csv", mode='r') as file:
        data = file.readlines()

    suma = 0
    for line in data:
        line = line.strip().split("	")
        suma += int(line[1])

    
    return suma
