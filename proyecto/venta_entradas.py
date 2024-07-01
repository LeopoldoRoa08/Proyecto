import random
from boleto import Boleto, Boleto_general, Boleto_vip
from cliente import Cliente
from equipo import Equipo
from estadio import Estadio
from partido import Partido
import mostrar_partidos
import mostrar_asientos                                           #Importamos los modulos necesarios
import archivo_json                            


def inicio_sesion(clientes: list[Cliente], partidos: list[Partido], equipos: list[Equipo], estadios: list[Estadio], boletos: list[Boleto]):
    while True:
        nuevo_usuario = es_nuevo_usuario()
        if nuevo_usuario is None:
            break

        if nuevo_usuario:
            nombre = preguntar("Ingrese nombre: ")                               #Le pedimos al usuario, que ingrese sus datos
            ci = preguntar_numero("Ingrese ci: ")
            contrasena = preguntar("Ingrese contrasena: ")
            age = preguntar_numero("Ingrese edad: ")
            #TODO: validar que no exista ya un cliente con la cedula que ingresó el usuario 
            for cliente in clientes:
                if cliente.ci == ci:
                    print("Ya existe un usuario con esa cedula")
                    continue
            nuevo_cliente = Cliente(nombre, age, ci, contrasena)                         #Verificamos si su cedula es unica
            clientes.append(nuevo_cliente)
        else:
            nuevo_cliente = iniciar_sesion(clientes)

        if nuevo_cliente:
            partido_seleccionado = preguntar_partido_especifico(partidos, equipos)      
            print("va a preguntar si es vip")
            es_vip = preguntar_tipo_entrada()

            asiento_seleccionado = preguntar_asientos(estadios,partido_seleccionado,es_vip,boletos) 

            # es_vampiro = nuevo_cliente.su_cedula_es_vampiro()
            # print("Es vampiro" if es_vampiro else "No es vampiro")

            if es_vip:
                precio = nuevo_cliente.imprimir_precio(75)                #Hacemos un condicional,para verificar si desea el modo Vip, o el modo general
            else:
                precio = nuevo_cliente.imprimir_precio(35)
            
            quiere_comprarlo = nuevo_cliente.quiere_comprarlo()

            if not quiere_comprarlo:
                seguir = quiere_seguir()
                if seguir:
                    continue
                else:
                    break
            
            if es_vip:
                boleto = Boleto_vip(generar_id(boletos),asiento_seleccionado,nuevo_cliente.ci,partido_seleccionado)  
            else:
                boleto = Boleto_general(generar_id(boletos),asiento_seleccionado,nuevo_cliente.ci,partido_seleccionado)
            
            boleto.precio = precio
            boletos.append(boleto)
            print(f"asiento {str(asiento_seleccionado)} comprado exitosamente")
            print(f"El codigo unico de su boleto es {boleto.id}")
            print(boletos)
            archivo_json.escribir_en_json(equipos,partidos,estadios,clientes,boletos)

def generar_id(boletos: list[Boleto]):                #Se realiza una funcion para generar el  id
    
    while True:
        id = random.randint(10000, 99999)
        se_repite = False
        for boleto in boletos:
            if boleto.id == id:
                se_repite = True
        
        if not se_repite:
            return id

def preguntar_asientos(estadios,partido_seleccionado,es_vip,boletos):   # Con esta funcion, el usario puede elegir su aciento predilecto
    while True:
        try:
            print("Elije uno: ")
            asientos = mostrar_asientos.mostrar_asientos(estadios,partido_seleccionado,es_vip,boletos)
            asiento = int(input("> "))

            if asiento in asientos:
                return asiento
            print("Asiento inválido")
        except Exception as e:
            print(e)


def preguntar_tipo_entrada():          #Le preguntamos al usario, si desea ser VIP o no   
    while True:
        try:
            pregunta = input("Es vip? (y o n): ")
            if pregunta.lower() == "y": return True
            if pregunta.lower() == "n": return False
        except:
            pass



def preguntar_partido_especifico(partidos, equipos):  #Con esta funcion, le preguntas el partido especifico que quiere escojer el usuario
    while True:
        try:
            print("Elige el partido que desees comprar sus entradas:")
            mostrar_partidos.mostrar_partidos_con_indice(partidos, equipos)
            pregunta = int(input("> "))
            print("lo va a buscar")
            partido_seleccionado = partidos[pregunta - 1]
            print("lo encontro")
            return partido_seleccionado
        except Exception as e:
            print("error")
            pass


def iniciar_sesion(clientes: list[Cliente]):  #Verificamos si el cliente existe
    while True:
        try:
            cedula = int(input("ingrese cedula: "))
            password = input("ingrese contrasenia: ")

            for cliente in clientes:
                if cliente.ci == cedula and cliente.password == password:
                    return cliente
            print("Ese cliente no existe")
            continuar = input("¿Volver a intentar? (y or n):")
            if continuar == "n":
                return False
        except:
            pass


def preguntar(mensaje: str):                    #Pregunta si el usuario quiere continuar  o no
    while True:
        try:
            pregunta = input(mensaje)

            if pregunta == "":
                continue

            return pregunta
        except:
            pass

def preguntar_numero(mensaje: str):          #Realizamos esta  funcion para preguntar su numero de id
    while True:
        try:
            pregunta = int(input(mensaje))
            return pregunta
        except:
            pass



def es_nuevo_usuario():                 # Realizamos esta funcion para verificar si es nuevo usario
    while True:
        pregunta = input('''¿Que quieres hacer=
1.- Iniciar sesión
2.- Registrarme
3.- Volver
> ''')
        if pregunta == '1':
            return False
        elif pregunta == "2":
            return True
        elif pregunta == "3":
            return None
        

def quiere_seguir():                         #Hacemos una funcion, preguntandole al usuario si quiere seguir
    while True:
        seguir = input('''Quiere seguir?
1. Si
2. No
> ''') 
        if seguir == "1":
            return True
        if seguir == "2":
            return False