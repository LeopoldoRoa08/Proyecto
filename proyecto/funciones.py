from partido import Partido                 #Importamos la clase partido


def get_partido(partidos: list[Partido], id_partido):            #Hacemos la funcion para obtener las id de los partidos
    for p in partidos:
        if p.id == id_partido:
            return p
