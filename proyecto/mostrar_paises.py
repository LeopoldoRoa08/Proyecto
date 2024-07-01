from equipo import Equipo
from partido import Partido #Importamos la clase Partido y Equipo



def mostrar_todos_los_paises_con_indices(partidos: list[Partido], equipos: list[Equipo]):  # Permite mostrar los indices de los paises
    indice = 1
    for partido in partidos:
        print(str(indice) + f". {partido.get_home(equipos)}")
        indice += 1