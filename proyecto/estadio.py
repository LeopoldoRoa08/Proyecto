from restaurante import Restaurante  #Importamos la clase restaurante


class Estadio():
    def __init__(self, id: str,name: str,city: str,capacity: list[int],restaurantes: list[Restaurante]) -> None:    #Definimos la clase estadio con sus atributos
        self.id = id
        self.name = name
        self.city = city
        self.capacity = capacity
        self.restaurantes = restaurantes
    
    def __str__(self):                     # Hacemos una funcion, que solo puede imprimir el nombre
        return f'name: {self.name}'
    
    def get_productos(self):               # Se realiza otra funcion para poder obtener los productos
        productos = []
        for restaurante in self.restaurantes:
            for producto in restaurante.productos:
                productos.append(producto)

        return productos