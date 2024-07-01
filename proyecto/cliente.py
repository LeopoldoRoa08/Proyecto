import itertools        #Esta funcion retorna un iterador proporcionando todas las combinaciones de r-tuplas de los elementos contenidos en iterable.


class Cliente:            # Definimos la clase cliente 
    def __init__(self, name: str, age: int, ci: int, password: str):
        self.name = name
        self.age = age
        self.ci = ci
        self.password = password
        self.precios_productos_comprados = []
    
    def su_cedula_es_vampiro(self):  # Verificamos si la cedula es un vampiro, con esta funcion
        cedula = self.ci
        lista = []
        for numero in str(cedula):
            lista.append(numero)
        permutations = list(itertools.permutations(lista))

        if len(str(cedula)) % 2 != 0:
            return False

        for permu in permutations:
            mitad = len("".join(permu)) // 2           # Recorremos esta lista, para verificar todas las combinaciones y asi asegugarnos de buscar el numero vampiro
            numero_1 = int("".join(permu[:mitad]))
            numero_2 = int("".join(permu[mitad:]))
    
            if numero_1*numero_2 == cedula:
                return True
        return False
    
    def imprimir_precio(self, precio: int):                # Funcion que nos permite saber el precio de la compra
        print("El precio de la compra inicial es: $", precio)

        if self.su_cedula_es_vampiro():                      # Este condicional nos ayuda a imprimir, el mensaje cuando el numero de la cedula es vampiro
            precio = precio / 2
            print("Como su numero es vampiro, recibirá un descuento del 50%", str(precio))
        
        precio = precio*0.16 + precio
        print(f"El precio de su boleto seria {precio}")
        return precio
    
    def quiere_comprarlo(self):               # Realizamos esta funcion, para poder asegurarnos de que el cliente, quiera hacer la compra
        while True:
            quiere = input('''Quiere comprarlo?
1.- Si
2.- No
> ''')
            if quiere == "1":
                return True
            
            if quiere == "2":
                return False
     
    def su_cedula_es_perfecta(self):        # Realizamos la funcion, para verificar si la cedula es perfecta
        divisores = []

        for i in range (1,self.ci):
            "dentro del for"
            if self.ci % i == 0:
                divisores.append(i)

        suma = 0

        for numero in divisores:
            suma += numero
        return suma == self.ci

    def imprimir_precio_producto_restaurante(self, precio):        # Esta funcion nos permite, imprimir el precio resultante
        print("El precio de la compra inicial es: $", precio)

        if self.su_cedula_es_perfecta():
            precio = precio + precio*0.15
            print("Como su cedula es perfecta, recibirá un descuento del 15%", str(precio))
        
        precio = precio*0.16 + precio
        print(f"El precio de su boleto seria {precio}")


        return precio