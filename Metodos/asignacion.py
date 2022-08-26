from Clases.materias import Materia
from Clases.salon import Salon


class Asignacion():
    asignacion = {"materia": "salon"}

    def materia_builder(self,nombreMateria,tiempoentrada,tiemposalida,profesor):
        materia = Materia(nombreMateria,tiempoentrada,tiemposalida,profesor)
        return materia

    def salon_builder(self,edificio, nombre):
        salon = Salon(edificio, nombre)
        return salon


