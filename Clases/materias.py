from datetime import *
class Materia:
    nombreMateria=None
    tiempoentrada=datetime(0,0,0,0,0,0,0)
    tiemposalida=datetime(0,0,0,0,0,0,0)
    horaSalida=None
    minutoSalida=None
    profesor=None

    def __init__(self,nombreMateria,tiempoentrada,tiemposalida,profesor):
        self.nombreMateria= nombreMateria
        self.tiempoentrada=tiempoentrada
        self.tiemposalida=tiemposalida
        self.profesor=profesor

    def get_nombreMateria(self):
        return self.nombreMateria

    def get_profesor(self):
        return self.profesor

    def get_tiempoentrada(self):
        return self.tiempoentrada

    def get_tiemposalida(self):
        return self.tiemposalida

    def set_nombreMateria(self,x):
        self.nombreMateria=x

    def set_profesor(self,x):
        self.profesor=x

    def set_tiempoentrada(self,x):
        self.tiempoentrada=x

    def settiemposalida(self,x):
        self.tiemposalida=x











