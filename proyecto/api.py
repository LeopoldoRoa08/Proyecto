import requests
from equipo import Equipo               #Importamos las clases y los modulos necesarios
from estadio import Estadio
from partido import Partido
from producto import Alimento, Bebida, Producto
from restaurante import Restaurante

def leer_equipos():#Hacemos una funcion, para poder obtener el url, y obetener los datos de la api de equipos
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
    return data

def crear_equipos(): #Registramos los datos de equipo en una lista
    data = leer_equipos()
    equipos = []
    equipos: list[Equipo] 

    for equipo in data:
        nuevo_equipo = Equipo(equipo["id"],equipo["code"],equipo["name"], equipo["group"])
        equipos.append(nuevo_equipo)
    return equipos

def leer_partidos():  #Hacemos una funcion, para poder obtener el url, y obetener los datos de la api de partidos
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json"
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
    return data

def crear_partidos():     #Registramos los datos de partido en una lista
    data = leer_partidos()
    partidos = []
    partidos: list[Partido]  
    for partido in data:#Recorremos esa lista y creamos la instacia de la clase Partido 
        nuevo_partido = Partido(partido["id"],partido["number"],partido["home"]["id"], partido["away"]["id"],partido["date"],partido["group"], partido["stadium_id"])
        partidos.append(nuevo_partido)
    return partidos

def leer_estadios():  #Hacemos una funcion, para poder obtener el url, y obetener los datos de la api de estadios
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json"
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
    return data

def crear_estadios():  #Registramos los datos de partido en una lista
    data = leer_estadios()

    estadios = []
    for estadio in data:
        restaurantes = []  # Recorremos la lista de restaurantes
        for restaurante in estadio["restaurants"]:
            productos = []
            productos: list[Producto]
            for producto in restaurante["products"]:  # Recorremos la lista de producto
                
                if producto["adicional"] == "alcoholic" or producto["adicional"] == "non-alcoholic":   #Hacemos un condicional, para crear las instacias de las clases hijas de producto
                    nuevo_producto = Bebida(producto["name"], producto["quantity"], producto["price"], producto["stock"], producto["adicional"])
                elif producto["adicional"] == "plate" or producto["adicional"] == "package":
                    nuevo_producto = Alimento(producto["name"], producto["quantity"], producto["price"], producto["stock"], producto["adicional"])
                productos.append(nuevo_producto)
            nuevo_restaurante = Restaurante(restaurante["name"],productos)
            restaurantes.append(nuevo_restaurante)
        nuevo_estadio = Estadio(estadio["id"],estadio["name"],estadio["city"],estadio["capacity"],restaurantes)
        estadios.append(nuevo_estadio)
    return estadios


