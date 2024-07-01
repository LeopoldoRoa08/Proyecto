import api
from boleto import Boleto
import buscar_partidos
from cliente import Cliente
import venta_entradas
import asistencia_al_partido
import show_productos                         #Importamos nuestras clases
import comprar_producto
import archivo_json
import estadisticas

def main():       # Definimos nuestro metodo main
    equipos, partidos, estadios, clientes, boletos = None,None,None,None,None        
    while True:
        pregunta = input("""Cargamos el programa desde 0?
1.- Si, quiero cargarlos desde 0
2.- No, quiero conservar mis datos                                         
> """)                                                                  #Preguntamos si el Usario quieres datos de cero o lo quiere guardar

        if pregunta == "1":
            equipos = api.crear_equipos()
            partidos = api.crear_partidos()
            estadios = api.crear_estadios()
            clientes = []
            clientes: list[Cliente]
            boletos = []
            boletos: list[Boleto]
            archivo_json.escribir_en_json(equipos,partidos,estadios, clientes, boletos)
            break
        elif pregunta == "2":
            equipos, partidos, estadios, clientes, boletos = archivo_json.leer_json()              # Si el usario, quiere conservar sus datos, estos se guardan desde un archivo json
            break
        
    while True:
        try:

            inicio = input('''¿Que quieres hacer?
1.- Buscar partidos
2.- Comprar entradas
3.- Asistencia al partido
4.- Mostrar productos vip de los restaurantes de un partido
5.- Comprar producto
6.- Estadisticas
7.- Volver
> ''')
    
            if inicio == "1":
                buscar_partidos.buscar_partidos(partidos, equipos, estadios)                                                # Hacemos un menu, y apartir de lo que decida el usario por teclado, el programa le va a ir mostrando los diferentes modulos 
            elif inicio == "2":
                venta_entradas.inicio_sesion(clientes,partidos, equipos, estadios, boletos)
            elif inicio == "3":
                asistencia_al_partido.asistencia_al_partido(boletos)
            elif inicio == "4":
                show_productos.show_productos(partidos,equipos, estadios)
            elif inicio == "5":
                comprar_producto.comprar_producto(estadios, boletos, clientes,partidos, equipos)
            elif inicio == "6":
                estadisticas.estadisticas(clientes,boletos,partidos,equipos, estadios)
            elif inicio == "7":
                break
        

            archivo_json.escribir_en_json(equipos,partidos,estadios, clientes, boletos)
        except Exception as e:
            print(e)

main()