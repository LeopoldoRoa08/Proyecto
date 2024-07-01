from boleto import Boleto
from estadio import Estadio
from partido import Partido       #Importamos las clases de Boleto,Estadio y Partido


def mostrar_asientos(estadios: list[Estadio], partido: Partido, es_vip: bool, boletos: list[Boleto]):       #Realizamos una funcion, que nos permita vizualizar los asientps, recorriendo la lista de asientos
    estadio = partido.get_estadio(estadios)
    nro_asientos = estadio.capacity[0 if not es_vip else 1]
    asientos = []
    for numero_asiento in range(1, nro_asientos + 1):
        for boleto in boletos:
            if boleto.asiento == numero_asiento and boleto.cliente_ci == partido.id:
                numero_asiento = "ocupado"
        asientos.append(numero_asiento)
    columna = 1

    for asiento in asientos:
        if columna <= 10:
            print(asiento,end="- ")
            columna += 1
        else:
            print("\n"+str(asiento),end="- ")
            columna = 2
    return asientos

    
