from estadio import Estadio  # Importamos la clase estadio
from producto import Producto  #Importamos la clase Producto


def mostrar_productos_recibiendo_estadio_con_indice(estadio: Estadio):  #Se realiza esta funcion, para indicar el indice de los producto, recorriendo la lista de productos y restaurantes
    lista_productos = []
    lista_productos: list[Producto]
    restaurante_de_la_lista_de_productos = None
    indice = 1
    for restaurante in estadio.restaurantes:
        restaurante_de_la_lista_de_productos = restaurante
        for producto in restaurante.productos:
            print(str(indice) + ".-", producto.name)
            indice += 1
            lista_productos.append(producto)
    
    return lista_productos, restaurante_de_la_lista_de_productos

