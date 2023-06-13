
class Fecha:
    def __init__(self, anho:int=2023, mes:int=5, dia:int=2):
        self.anho=anho
        self.mes=mes
        self.dia=dia

    def __repr__(self) -> str:
        return f'{self.dia}/{self.mes}/{self.anho}'
    
class Persona:
    def __init__(self, apellido='', nombre='', nacimiento:Fecha=None):
        self.apellido=apellido
        self.nombre=nombre
        self.nacimineto=nacimiento
    def __repr__(self):
        return f'Persona -> nombre={self.nombre} apellido={self.apellido} nacimiento={self.nacimineto}'
