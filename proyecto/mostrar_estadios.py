from estadio import Estadio  # Importamos la clase Estadio


def mostrar_todos_los_estadios_con_indices(estadios: list[Estadio]): #Realizamos una funcion, cuyo fin es recorrer los indices de los estadios
    indice = 1
    for estadio in estadios:
        print(str(indice) + f". {estadio}")
        indice += 1