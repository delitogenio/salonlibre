from Clases.Usuarios.usuarios import Usuario
from Metodos.asignacion import VerAsignacion
from flaskr.Metodos.DBConnection import connection



class Estudiante (Usuario,VerAsignacion):

    def verasignacion(self,parametro):
        conn = connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Asignacion")
        print()
        for (nombreMateria) in self.cur:
            if parametro in nombreMateria:
                print("La asignacion es " + str(nombreMateria[1]))
            else:
                "La asignacion no existe"


