from equipo import Equipo
from estadio import Estadio
from partido import Partido
import mostrar_paises
import mostrar_partidos
import mostrar_estadios                             #Importamos las clases y los modulos necesarios
import mostrar_fechas

def buscar_partidos(partidos: list[Partido], equipos: list[Equipo], estadio: list[Estadio]):

    while True:
        try:
            opcion = input('''¿Como desea buscar los partidos?
a. Buscar todos los partidos de un país
b. Buscar todos los partidos que se jugarán en un estadio específico
c. Buscar todos los partidos que se jugarán en una fecha determinada
d. Deseo volver
> ''')
            if opcion.lower() == "a":
                buscar_partidos_de_un_pais(partidos, equipos)
            elif opcion.lower() == "b":
                buscar_partidos_de_un_estadio(partidos,equipos,estadio)                 #Le pedimos al usario que elija especificamente, que  partidos desea buscar
            elif opcion.lower() == "c":
                buscar_partidos_de_una_fecha(partidos,equipos)
            elif opcion.lower() == "d":
                break
        except:
            pass

def buscar_partidos_de_un_pais(partidos: list[Partido], equipos: list[Equipo]):            # Realizamos una funcion que nos ayudara a buscar los partidos de un pais, en especifico
    while True:
        try:
            print("Elige el pais del cual desees saber sus partidos")
            mostrar_paises.mostrar_todos_los_paises_con_indices(partidos, equipos)
            pregunta = int(input("> "))

            id_pais_seleccionado = partidos[pregunta -1].home

            partidos_filtrados = []
            for partido in partidos:
                if partido.home == id_pais_seleccionado:
                    partidos_filtrados.append(partido)
                
                if partido.away == id_pais_seleccionado:
                    partidos_filtrados.append(partido)
            
            print("Estos son los partidos que jugara el pais seleccionado:")
            mostrar_partidos.mostrar_partidos(partidos_filtrados, equipos)
            break
        except Exception as e:
            print(e)

def buscar_partidos_de_un_estadio(partidos: list[Partido], equipos: list[Equipo], estadios: list[Estadio]):      # Realizamos una funcion que nos ayudara a buscar los partidos de una fecha, en especifico
    while True:
        try:
            print("ingrese un estadio")
            mostrar_estadios.mostrar_todos_los_estadios_con_indices(estadios)
            pregunta = int(input("> "))

            estadio = estadios[pregunta - 1]
            partidos_filtrados = []
            for partido in partidos:
                if partido.stadium_id == estadio.id:
                    partidos_filtrados.append(partido)
            
            print("Estos son los partidos que se van a jugar en ese estadio")
            mostrar_partidos.mostrar_partidos(partidos, equipos)
            break
        except Exception as e:
            pass

def buscar_partidos_de_una_fecha(partidos: list[Partido], equipos: list[Equipo]):
    while True:
        try:
            print("Elija la fecha que desee ver los partidos")
            fechas = mostrar_fechas.mostrar_fechas_con_indices(partidos)
            pregunta = int(input("> "))
            
            fecha = fechas[pregunta - 1]
            partidos_filtrados = []
            for partido in partidos:
                if partido.date == fecha:
                    partidos_filtrados.append(partido)
            
            mostrar_partidos.mostrar_partidos(partidos_filtrados, equipos)
            break
        except:
            pass