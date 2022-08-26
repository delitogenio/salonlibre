from espacio import Espacio


class Laboratorio(Espacio):

    def __init__(self):
        self.edificio=''
        self.nombre=''

    def get_edificio(self):
        return self.edificio

    def get_nombre(self):
        return self.nombre

    def set_edificio(self, x):
        self.edificio = x

    def set_nombre(self, x):
        self.nombre = x