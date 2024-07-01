class Equipo():    #Definimos la clase equipo con sus atributos
    def __init__(self, id: str, code: str, name: str, group: str) -> None:
        self.id = id
        self.code = code
        self.name = name
        self.group = group

    def __str__(self):  # Hacemos una funcion para imprimir por pantalla nombre y codigo 
        return f"{self.name} - {self.code}"