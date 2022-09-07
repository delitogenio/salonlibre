from Clases.Usuarios.usuarios import Usuario
from Clases.Asignaciones.asignacionClase import AsignacionClase
from Metodos.asignacion import VerAsignacion, SolicitarAsignacion, CrearAsignacion

class Administrativo(Usuario, VerAsignacion, SolicitarAsignacion,CrearAsignacion):

    def verasignacion(self, parametro):
        asignacion = AsignacionClase()
        asignacion.set_parametro(parametro)
        asignacion.verasignacion()

    def crearasignacion(self, nombreMateria, profesor, edifcio, nombreespacio, tiempoentrada,
                        tiemposalida, tipoespacio):
        asignacion = AsignacionClase()
        asignacion.set_asignacion(nombreMateria, profesor ,edifcio ,nombreespacio,tiempoentrada,tiemposalida,tipoespacio)
        asignacion.crearasignacion()

    def solicitarasignacion(self):
        pass





