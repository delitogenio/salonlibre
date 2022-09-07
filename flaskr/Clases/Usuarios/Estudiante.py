from Clases.Usuarios.usuarios import Usuario
from Metodos.asignacion import VerAsignacion
from flaskr.Metodos.DBConnection import connection
from Clases.Asignaciones.asignacionClase import AsignacionClase



class Estudiante (Usuario,VerAsignacion):

    def verasignacion(self,parametro):
        asignacion = AsignacionClase()
        asignacion.set_parametro(parametro)
        asignacion.verasignacion()


