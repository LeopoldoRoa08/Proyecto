from equipo import Equipo  #Importamos la clase Equipo
from partido import Partido #Importamos la clase Partido


def mostrar_partidos(partidos: list[Partido], equipos: list[Equipo]):  #Nos permite mostrar los partidos que va hacer ese equipo, en especifico
    for partido in partidos:
        print(partido.get_home(equipos), "vs", partido.get_away(equipos))

def mostrar_partidos_con_indice(partidos: list[Partido], equipos: list[Equipo]): #Nos permite mostrar los indices de esos partidos
    indice = 1
    for partido in partidos:
        print(str(indice)+".-",partido.get_home(equipos), "vs", partido.get_away(equipos))
        indice += 1