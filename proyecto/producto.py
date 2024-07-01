class Producto:     #Definimos la clase producto con sus atributos
    def __init__(self, name: str, quantity: int,price: str,stock: int,adicional: str) -> None:
        self.name = name
        self.quantity = quantity
        self.price = price
        self.stock = stock
        self.adicional = adicional
    
    def __str__(self):  #Returnamos los atributos de nombre y precio,para que se puedan ver en Pantalla
        return f"nombre: {self.name} precio: {self.price}"
    
    def descontar_una_unidad(self):
        if self.quantity > 0:
            self.quantity -= 1
        elif self.stock > 0:
            self.stock -= 1
        else:
            print("No hay stock")

    def obtener_precio(self):                
        return self.price*0.16 + self.price

class Bebida(Producto):           #Heredamos de la clase Producto,la clase Bebida
    def __init__(self, name: str, quantity: int, price: str, stock: int, adicional: str) -> None:       
        super().__init__(name, quantity, price, stock, adicional)

class Alimento(Producto):        #Heredamos de la clase Producto,la clase Alimento
    def __init__(self, name: str, quantity: int, price: str, stock: int, adicional: str) -> None:
        super().__init__(name, quantity, price, stock, adicional)