#This is the interface asignacion method
import abc


class CrearAsignacion(abc.ABC):

    @abc.abstractmethod
    def crearasignacion(self):
        pass

class EliminarAsignacion(abc.ABC):

    @abc.abstractmethod
    def eliminarasignacion(self):
        pass


class ModificarAsignacion(abc.ABC):

    @abc.abstractmethod
    def modificarasignacion(self):
        pass


class VerAsignacion(abc.ABC):
    @abc.abstractmethod
    def verasignacion(self,parametro):
        pass


