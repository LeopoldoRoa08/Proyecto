import json
import funciones

from boleto import Boleto, Boleto_general, Boleto_vip
from cliente import Cliente
from equipo import Equipo
from estadio import Estadio
from partido import Partido
from producto import Alimento, Bebida, Producto
from restaurante import Restaurante


def escribir_en_json(equipos: list[Equipo], partidos: list[Partido], estadios: list[Estadio], clientes: list[Cliente], boletos: list[Boleto, Boleto_vip, Boleto_general]):
    data = {}
    data["equipos"] = []
    data["partidos"] = []
    data["estadios"] = []
    data["clientes"] = []
    data["boletos"] = []


    for equipo in equipos:
        diccionario = {
            "id": equipo.id,
            "code": equipo.code,
            "name": equipo.name,
            "group": equipo.group            
        }
        data["equipos"].append(diccionario)
    
    for partido in partidos:
        diccionario = {
            "id": partido.id,
            "number": partido.number,
            "home": partido.home,
            "away": partido.away,
            "date": partido.date,
            "group": partido.group,
            "stadium_id": partido.stadium_id            
        }

        data["partidos"].append(diccionario)

    for estadio in estadios:
        diccionario = {
            "id": estadio.id,
            "name": estadio.name,
            "city": estadio.city,
            "capacity": estadio.capacity,
            "restaurantes": [],        
        }

        for restaurante in estadio.restaurantes:
            dic_restaurante = {
                "name": restaurante.name,                
                "productos": []                    
            }
            for producto in restaurante.productos:
                dic_producto = {
                    "name": producto.name,
                    "quantity": producto.quantity,
                    "price": producto.price,
                    "stock": producto.stock,
                    "adicional": producto.adicional
                }
                dic_restaurante["productos"].append(dic_producto)
            diccionario["restaurantes"].append(dic_restaurante)
        
        data["estadios"].append(diccionario)
    
    for cliente in clientes:
        diccionario = {
            "name": cliente.name,
            "age": cliente.age,
            "ci": cliente.ci,
            "password": cliente.password,
            "precios_productos_comprados": cliente.precios_productos_comprados,
        }
        data["clientes"].append(diccionario)

    for boleto in boletos:
        diccionario = {
            "id": boleto.id,
            "precio": boleto.precio,
            "asiento": boleto.asiento,
            "cliente_ci": boleto.cliente_ci,
            "partido": boleto.partido.id,
            "asistio": boleto.asistio,
            "es_vip": isinstance(boleto,Boleto_vip)            
        }
        data["boletos"].append(diccionario)

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
    


def leer_json():

    with open('data.json', 'r') as file:
        data = json.load(file)
        equipos = data["equipos"]
        equipos_actualizado = []
        for equipo in equipos:
            nuevo_equipo = Equipo(equipo["id"],equipo["code"],equipo["name"],equipo["group"])
            equipos_actualizado.append(nuevo_equipo)


        partidos = data["partidos"]
        partidos_actualizado = []
        for partido in partidos:
            nuevo_partido = Partido(partido["id"], partido["number"], partido["home"], partido["away"], partido["date"], partido["group"], partido["stadium_id"])
            partidos_actualizado.append(nuevo_partido)

        estadios = data["estadios"]
        estadios_actualizado = []
        for estadio in estadios:
            lista_restaurantes = []
            for restaurante in estadio["restaurantes"]:
                lista_productos = []
                for producto in restaurante["productos"]:
                    if producto["adicional"] == "alcoholic" or producto["adicional"] == "non-alcoholic":
                        nuevo_producto = Bebida(producto["name"], producto["quantity"], producto["price"], producto["stock"], producto["adicional"])
                    else:
                        nuevo_producto = Alimento(producto["name"], producto["quantity"], producto["price"], producto["stock"], producto["adicional"])
                    lista_productos.append(nuevo_producto)
                nuevo_restaurante = Restaurante(restaurante["name"], lista_productos)
                lista_restaurantes.append(nuevo_restaurante)
            nuevo_estadio = Estadio(estadio["id"], estadio["name"], estadio["city"], estadio["capacity"], lista_restaurantes)
            estadios_actualizado.append(nuevo_estadio)
        



        clientes = data["clientes"]
        clientes_actualizado = []
        for cliente in clientes:
            nuevo_cliente = Cliente(cliente["name"], cliente["age"], cliente["ci"], cliente["password"])
            nuevo_cliente.precios_productos_comprados = cliente["precios_productos_comprados"]
            clientes_actualizado.append(nuevo_cliente)
       
        boletos = data["boletos"]
        boletos_actualizado = []
        for boleto in boletos:
            if boleto["es_vip"]:
                nuevo_boleto = Boleto_vip(boleto["id"], boleto["asiento"], boleto["cliente_ci"], funciones.get_partido(partidos_actualizado, boleto["partido"]))
                nuevo_boleto.asistio = boleto["asistio"]
                nuevo_boleto.precio = boleto["precio"]
            else:
                nuevo_boleto = Boleto_general(boleto["id"], boleto["asiento"], boleto["cliente_ci"], boleto["partido"])
                nuevo_boleto.asistio = boleto["asistio"]
                nuevo_boleto.precio = boleto["precio"]
            boletos_actualizado.append(nuevo_boleto)
        
        return equipos_actualizado, partidos_actualizado, estadios_actualizado, clientes_actualizado, boletos_actualizado
    
equipos, partidos, estadios, clienteso, boletos = leer_json()

