#This is the interface asignacion method
import abc


class CrearAsignacion(abc.ABC):
    @abc.abstractmethod
    def crearasignacion(self, nombremateria, profesor, edifcio, nombreespacio, tiempoentrada,
                        tiemposalida, tipoespacio):
        pass

class EliminarAsignacion(abc.ABC):

    @abc.abstractmethod
    def eliminarasignacion(self,codigo):
        pass


class ModificarAsignacion(abc.ABC):

    @abc.abstractmethod
    def modificarasignacion(self):
        pass


class VerAsignacion(abc.ABC):
    @abc.abstractmethod
    def verasignacion(self,parametro):
        pass




