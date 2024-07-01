from equipo import Equipo
from estadio import Estadio
import mostrar_partidos                                   # Importamos los modulos y clases necesarios
from partido import Partido
from producto import Alimento, Bebida, Producto

def show_productos(partidos: list[Partido], equipos: list[Equipo], estadios: list[Estadio]):               #Le damos al usuario, la opcion de elegir que tipo de producto quiere ver
    while True:
        try:
            mostrar_partidos.mostrar_partidos_con_indice(partidos, equipos)
            print("De cual partido te gustaria ver los productos?:")
            indice = int(input("> : "))

            partido = partidos[indice-1]

            pregunta = input('''Buscar productos por
1.- nombre
2.- tipo
3.- rango de precio
4.- No quiero, quiero volver
> ''')
            
            if pregunta == "1":
                products = buscar_producto_por_nombre(partido.get_estadio(estadios))                        
                for producto in products:
                    print(producto)
            elif pregunta == "2":
                buscar_producto_por_tipo(partido.get_estadio(estadios))
            elif pregunta == "3":
                print("entro")
                estadio = partido.get_estadio(estadios)
                productos = estadio.get_productos()
                lista = buscar_producto_por_rango_de_precio(productos)
                for producto in lista:
                    print(producto)
            elif pregunta == "4":
                break
            
            continuar = input("""\nContinuar operaciones?
1.- Si
2.- No
> """)
            if continuar == "2":
                break
        except Exception as e:
            print(e)

def buscar_producto_por_nombre(estadio: Estadio):                                               # Aqui recorrimos una lista para buscar el producto por su nombre     
    while True:
        try:
            nombre = input("Ingrese nombre producto")
            
            lista = []
            lista: list[Producto]

            for restaurante in estadio.restaurantes:
                for producto in restaurante.productos:
                    if nombre.lower() in producto.name.lower():
                        lista.append(producto)
            return lista
        except Exception as e:
            print(e)

def buscar_producto_por_tipo(estadio: Estadio):                                               # Aqui recorrimos una lista para buscar el producto por tipo
    while True:
        try:
            tipo = input('''Ingrese tipo producto
1.- Bebida
2.- Alimento
> ''')
            productos = []
            productos: list[Producto]

            if tipo != "1" and tipo != "2":
                print("Dato invalido")
                continue
            
            for restaurante in estadio.restaurantes:
                for producto in restaurante.productos:
                    
                    if isinstance(producto, Bebida) and tipo == "1":
                        productos.append(producto)
                    
                    if isinstance(producto, Alimento) and tipo == "2":
                        productos.append(producto)
            
            tipos = []

            for producto in productos:
                if producto.adicional not in tipos:
                    tipos.append(producto.adicional)
            
            print("Elije un tipo de producto por ver")
            indice = 1
            for tipo in tipos:
                print(f'{str(indice) + " " + tipo}')
                indice += 1

            id = int(input("> "))
            tipo = tipos[id - 1]

            for producto in productos:
                if producto.adicional == tipo:
                    print(producto)
            
            break
        except Exception as e:
            print(e)

def buscar_producto_por_rango_de_precio(productos: list[Producto]):                           # Aqui recorrimos una lista para buscar el producto por su rango de precio
    while True:
        try:
            print("brasil esta raro")
            maximo = int(input("Ingrese el maximo de precio: "))

            lista = []
            lista: list[Producto]
            for producto in productos:
                if float(producto.price) <= maximo:
                    lista.append(producto)
            return lista
            

        except Exception as e:
            print(e)

