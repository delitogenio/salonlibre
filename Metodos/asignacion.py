from Clases.materias import Materia
from Clases.salon import Salon


class Asignacion():
    codigo= None
    materia = Materia()
    salon = Salon()

    def __init__(self, codigo,materia, salon):
        self.codigo=codigo
        self.materia=materia
        self.salon=salon

    def set_asignacion(self,nombreMateria,tiempoentrada,tiemposalida,profesor,edifcio,nombreespacio):
        self.materia.set_nombreMateria(nombreMateria)
        self.materia.set_tiempoentrada(tiempoentrada)
        self.materia.settiemposalida(tiemposalida)
        self.materia.set_profesor(profesor)
        self.salon.set_edificio(edifcio)
        self.salon.set_nombre(nombreespacio)

    def get_codigo(self):
        return self.codigo






