from boleto import Boleto, Boleto_vip
from cliente import Cliente
from equipo import Equipo
from estadio import Estadio
import mostrar_partidos
from partido import Partido                               # Importamos los modulos y clases necesarios
from restaurante import Restaurante

def estadisticas(clientes: list[Cliente], boletos: list[Boleto], partidos: list[Partido], equipos: list[Equipo], estadios: list[Estadio]):
    while True:
        try:
            pregunta = input("""decide
1.- ¿Cuál es el promedio de gasto de un cliente VIP en un partido (ticket +
restaurante)?
2.- Mostrar tabla con la asistencia a los partidos de mejor a peor, mostrando el
nombre del partido (nombre de los equipos), estadio en donde se juega,
boletos vendidos, personas que asistieron y la relación asistencia/venta
3.- ¿Cuál fue el partido con mayor asistencia?
4.- ¿Cuál fue el partido con mayor boletos vendidos?
5.- Top 3 productos más vendidos en el restaurante.
6.- Top 3 de clientes (clientes que más compraron boletos)                        
7.- Volver
> """)                                                                          #Esta funcion permite al usuario, que escoja  que estadistica, desea ver
            if pregunta == "1":
                partido = preguntar_partido_especifico(partidos, equipos)
                print(f"-----------> {promedio_gasto_cliente_productos_por_partido(clientes,partido) + promedio_gasto_cliente_vip_tickets_por_partido(boletos, partido)}")
            elif pregunta == "2":
                mostrar_tabla_mejor_a_peor(clientes, boletos, partidos, equipos)
            elif pregunta == "3":
                mostrar_partido_con_mayor_asistencia(clientes, boletos, partidos, equipos)
            elif pregunta == "4":
                mostrar_partido_con_mayor_venta(clientes, boletos, partidos, equipos)
            elif pregunta == "5":
                mostrar_tres_productos_mas_vendidos_por_restaurante(clientes, boletos, partidos, equipos, estadios)
            elif pregunta == "6":
                clientes_que_mas_compraron_boletos(clientes, boletos, partidos, equipos, estadios)
            elif pregunta == "7":
                break
        except Exception as e:
            print(e)

def preguntar_partido_especifico(partidos, equipos):                               #Esta funcion permite, que el usuario escoja que partido desea ver 
    while True:
        try:
            print("Elige el partido que desees:")
            mostrar_partidos.mostrar_partidos_con_indice(partidos, equipos)
            pregunta = int(input("> "))
            partido_seleccionado = partidos[pregunta - 1]
            return partido_seleccionado
        except Exception as e:
            print("error")
            pass

def promedio_gasto_cliente_vip_tickets(boletos: list[Boleto]):                   # Se realiza esta funcion, que permite calcula el promedio de lo que gasta  un cliente vip
    dinero = 0
    cantidad = 0
    for boleto in boletos:
        if isinstance(boleto, Boleto_vip):
            dinero += boleto.precio
            cantidad += 1
    return dinero / cantidad

def promedio_gasto_cliente_vip_tickets_por_partido(boletos: list[Boleto], partido: Partido):     # Se realiza esta funcion, que permite calcula el promedio de lo que gasta  un cliente vip por partido
    dinero = 0
    cantidad = 0
    for boleto in boletos:
        if isinstance(boleto, Boleto_vip) and boleto.cliente_ci.id == partido.id:
            dinero += boleto.precio
            cantidad += 1
    return dinero / cantidad if cantidad != 0 else 0

def promedio_gasto_cliente_productos_por_partido(clientes: list[Cliente], partido: Partido):     # Se realiza esta funcion, que permite calcula el promedio de lo que gasta  un cliente en un producto
    dinero = 0
    cantidad = 0
    for cliente in clientes:
        for comprado in cliente.precios_productos_comprados:
            if comprado[4] == partido.id:
                dinero += comprado[3]
                cantidad += 1
    return dinero / cantidad if cantidad != 0 else 0

def mostrar_tabla_mejor_a_peor(clientes: list[Cliente], boletos: list[Boleto], partidos: list[Partido], equipos: list[Equipo]):       #Realizamos la tabla para poner la asistebcia de los partidos de mejor a peor
    lista_boletos_vendidos = []
    
    for boleto in boletos:
        if len(lista_boletos_vendidos) == 0:
            lista_boletos_vendidos.append([boleto.cliente_ci, 1])
        else:
            for indice in range(len(lista_boletos_vendidos)):
                if lista_boletos_vendidos[indice][0].id == boleto.cliente_ci:
                    lista_boletos_vendidos[indice][1] += 1
                    break
                elif indice == len(lista_boletos_vendidos) - 1:
                    lista_boletos_vendidos.append([boleto.cliente_ci, 1])
    
    lista_boletos_vendidos.sort(key=lambda x: x[1], reverse=True)
    
    for termino in lista_boletos_vendidos:
        print('******************')
        partido = termino[0]
        partido: Partido
        print(partido.get_home(equipos), partido.get_away(equipos))
        asistidos = 0
        vendidos = 0
        for boleto in boletos:
            if boleto.cliente_ci.id == partido.id:
                print(boleto.cliente_ci)
                if boleto.asistio:
                    asistidos += 1
                    vendidos += 1
                else:
                    vendidos += 1
        print(f"asistidos: {asistidos}")
        print(f"vendidos: {vendidos}")

def mostrar_partido_con_mayor_asistencia(clientes, boletos, partidos, equipos):                # Esta funcion, nos indica el partido con mayor asistencia
    lista_boletos_asistidos = []
    
    for boleto in boletos:
        if len(lista_boletos_asistidos) == 0:
            lista_boletos_asistidos.append([boleto.partido, 1])
        else:
            for indice in range(len(lista_boletos_asistidos)):
                if lista_boletos_asistidos[indice][0].id == boleto.partido.id and boleto.asistio:
                    lista_boletos_asistidos[indice][1] += 1
                    break
                elif indice == len(lista_boletos_asistidos) - 1:
                    lista_boletos_asistidos.append([boleto.partido, 1])
    
    lista_boletos_asistidos.sort(key=lambda x: x[1], reverse=True)

    
    partido = lista_boletos_asistidos[0][0]
    print(f"Partido {partido.get_home(equipos)} - {partido.get_away(equipos)}: {lista_boletos_asistidos[0][1]} asistencias")
    
    pass

def mostrar_partido_con_mayor_venta(clientes, boletos, partidos, equipos):                          # Esta funcion, nos indica el partido con mayor venta
    lista_boletos_vendidos = []
    
    for boleto in boletos:
        if len(lista_boletos_vendidos) == 0:
            lista_boletos_vendidos.append([boleto.partido, 1])
        else:
            for indice in range(len(lista_boletos_vendidos)):
                if lista_boletos_vendidos[indice][0].id == boleto.partido.id:
                    lista_boletos_vendidos[indice][1] += 1
                    break
                elif indice == len(lista_boletos_vendidos) - 1:
                    lista_boletos_vendidos.append([boleto.partido, 1])
    
    lista_boletos_vendidos.sort(key=lambda x: x[1], reverse=True)

    
    partido = lista_boletos_vendidos[0][0]
    print(f"Partido {partido.get_home(equipos)} - {partido.get_away(equipos)}: {lista_boletos_vendidos[0][1]} ventas")


    
    pass

def mostrar_tres_productos_mas_vendidos_por_restaurante(clientes, boletos, partidos, equipos, estadios):   #Realizamos esta funcion para que nos indique, los tres productos mas vendido de un restaurante
    while True:
        try:
            # productos = []
            estadios: list[Estadio]
            restaurantes = []
            restaurantes: list[Restaurante]
            for estadio in estadios:
                estadio: Estadio
                for restaurante in estadio.restaurantes:
                    restaurantes.append(restaurante)
                    # for produ in restaurante.productos:
                    #     productos.append([restaurante,produ])

            contador = 0
            for restaurante in restaurantes:
                print(str(contador),restaurante.name)
                contador += 1
            indice = int(input("Ingrese el restaurante que desee: "))

            rest = restaurantes[indice - 1]
            productos_del_restaurante = []
            for estadio in estadios:
                for restaurante in estadio.restaurantes:
                    for producto in restaurante.productos:
                        if rest.name == restaurante.name:
                            productos_del_restaurante.append(producto)
            # ............................


            lista_productos_vendidos = []        
            
            for cliente in clientes:
                for producto_comprado in cliente.precios_productos_comprados:
                    if len(lista_productos_vendidos) == 0:
                        lista_productos_vendidos.append([producto_comprado[2], 1])
                    else:
                        for indice in range(len(lista_productos_vendidos)):
                            if lista_productos_vendidos[indice][0] == producto_comprado[2]:
                                lista_productos_vendidos[indice][1] += 1
                                break
                            elif indice == len(lista_productos_vendidos) - 1:
                                lista_productos_vendidos.append([producto_comprado[2], 1])
            
            lista_productos_vendidos.sort(key=lambda x: x[1], reverse=True)
            
            contador = 0
            print("\n\n******************")
            for termino in lista_productos_vendidos:
                producto = termino[0]
                print(f"Producto {producto}: {termino[1]} ventas")
                contador += 1
                if contador == 3:
                    break
            print("******************\n\n")
            break
        except:
            pass

def clientes_que_mas_compraron_boletos(clientes, boletos, partidos, equipos, estadios):        # Realizamos esta funcion, para que nos  indique, los 3 clientes que mas compraron estos boletos
    lista_cantidad_compras_clientes = []
    
    for boleto in boletos:
        boleto: Boleto
        
        if len(lista_cantidad_compras_clientes) == 0:
            lista_cantidad_compras_clientes.append([boleto.cliente_ci, 1])
        else:
            for indice in range(len(lista_cantidad_compras_clientes)):
                if str(lista_cantidad_compras_clientes[indice][0]) == str(boleto.cliente_ci):
                    lista_cantidad_compras_clientes[indice][1] += 1
                    break
                elif indice == len(lista_cantidad_compras_clientes) - 1:
                    lista_cantidad_compras_clientes.append([boleto.cliente_ci, 1])
    
    lista_cantidad_compras_clientes.sort(key=lambda x: x[1], reverse=True)

    contador = 0
    for termino in lista_cantidad_compras_clientes:
        cliente = termino[0]
        print(f"Cedula {cliente}: {termino[1]} ventas")
        contador += 1
        if contador == 3: break
    




