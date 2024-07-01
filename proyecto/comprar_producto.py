from boleto import Boleto, Boleto_vip
from cliente import Cliente
from estadio import Estadio
import mostrar_estadios
import venta_entradas
import mostrar_productos                                 #Importamos las clases y los modulos necesarios

def comprar_producto(estadios: list[Estadio], boletos: list[Boleto], clientes: list[Cliente], partidos, equipos):  # Hacemos una funcion, que nos ayudara a poder comprar eñproducto y autenticar los boletos
    while True:
        try:
            print("Elige el estadio en el que quieras comprar boletos: ")
            mostrar_estadios.mostrar_todos_los_estadios_con_indices(estadios)
            indice = int(input("> ")) - 1

            estadio_elegido = estadios[indice]

            cedula = int(input("Ingrese su cedula: "))

            puede_comprar = False
            boleto_que_lo_certica = None
            for boleto in boletos:
                if boleto.cliente_ci == cedula and boleto.cliente_ci.stadium_id == estadio_elegido.id and boleto.asistio and isinstance(boleto,Boleto_vip):
                    puede_comprar = True
                    boleto_que_lo_certica = boleto
            
            if not puede_comprar:
                print("""No puede comprar productos en este partido por alguno de estos motivos
1. Su cedula puede no haber coincidico con ninguno de los boletos
2. Usted puede no tener boletos asociados a este estadio
3. No se ha verificado su asistencia al partido asociado al boleto de ese estadio""")
                
                if not venta_entradas.quiere_seguir(): 
                    break
                continue
            
            cliente_elegido = None
            for cliente in clientes:
                if cliente.ci == cedula:
                    cliente_elegido = cliente
            
            if not cliente_elegido:
                print("No se encontro un cliente con esa cedula")
                if not venta_entradas.quiere_seguir:
                    break
                continue
            

            print("Elije el producto que desees")
            lista_productos, restaurante_de_la_lista_de_productos = mostrar_productos.mostrar_productos_recibiendo_estadio_con_indice(estadio_elegido)
            indice = int(input("> "))
            
            producto_elegido = lista_productos[indice-1]


            precio = cliente_elegido.imprimir_precio_producto_restaurante(float(producto_elegido.price))

            quiere_comprarlo = cliente_elegido.quiere_comprarlo()

            if not quiere_comprarlo:
                seguir = venta_entradas.quiere_seguir()
                if seguir:
                    continue
                else:
                    break
            
            if producto_elegido.stock <= 0:
                print("Disculpe las molestias, el producto esta agotado")
                continue
            
            lista_productos.remove(producto_elegido)
            producto_elegido.descontar_una_unidad()
            lista_productos.append(producto_elegido)

            for estadio in estadios:
                for restaurante in estadio.restaurantes:
                    if restaurante == restaurante_de_la_lista_de_productos:
                        restaurante.productos = lista_productos
            
            clientes.remove(cliente_elegido)
            cliente_elegido.precios_productos_comprados.append([estadio_elegido.id,restaurante_de_la_lista_de_productos.name,producto_elegido.name,precio, boleto_que_lo_certica.cliente_ci.id])
            clientes.append(cliente_elegido)


            print("Usted ha comprado satisfactoriamente su producto")
            seguir = venta_entradas.quiere_seguir()
            if seguir:
                continue
            else:
                break

        except:
            pass

