from partido import Partido    # Importamos la clase partido


def mostrar_fechas_con_indices(partidos: list[Partido]): # Importamos la clase partido
    fechas = []
    indice = 1
    for partido in partidos:
        if partido.date not in fechas:
            fechas.append(partido.date)
            print(str(indice) + f") {partido.date}")
            indice += 1
    return fechas