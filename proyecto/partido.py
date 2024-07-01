from equipo import Equipo           #Importamos las clases de Equipo Y Estadio
from estadio import Estadio


class Partido():                  #Definimos la clase Partido, con sus atributos
    def __init__(self, id: str, number: int, home: str, away: str, date: str, group: str, stadium_id: str) -> None:
        self.id =id
        self.number =number
        self.home =home
        self.away =away
        self.date =date
        self.group =group
        self.stadium_id =stadium_id

    def __str__(self):             #Returnamos  el atributo de id, para que se puede imprimir bien el mensaje
        return f"id: {self.id}"
    
    def get_home(self, equipos: list[Equipo]):  #Realizamos una funcion, para obtener una lista del equipo local
        for equipo in equipos:
            if equipo.id ==  self.home:
                return equipo
        return None
    
    def get_away(self, equipos: list[Equipo]):  #Realizamos una funcion, para obtener una lista del equipo extranjero
        for equipo in equipos:
            if equipo.id ==  self.away:
                return equipo
        return None
    
    def get_estadio(self,estadios: list[Estadio]):  #Realizamos una funcion, para obtener una lista de todos los id del estadio
        for estadio in estadios:
            if self.stadium_id == estadio.id:
                return estadio
        return None
    