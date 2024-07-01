from producto import Producto              # Importamos la clase producto


class Restaurante():                       #Definimos la clase restaurante, con sus atributos  
    def __init__(self, name: str, productos: list[Producto]) -> None:      
        self.name = name        
        self.productos = productos        