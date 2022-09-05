import datetime

from Clases.laboratorio import Laboratorio
from Metodos.DBConnection import connection
from Clases.materias import Materia
from Clases.salon import Salon


class Asignacion():
    codigo = None
    materia = Materia()
    salon = Salon()
    lab = Laboratorio()
    tipoEspacio = None
    tiempoentrada = None
    tiemposalida = None
    conn = connection()
    cur = conn.cursor()

    def __init__(self, codigo, materia, salon, tiempoentrada, tiemposalida, tipoespacio):
        self.codigo = codigo
        self.materia = materia
        self.salon = salon
        self.tiempoentrada = datetime.datetime.strptime(tiempoentrada, '%Y-%m-%d %H:%M:%S')
        self.tiemposalida = datetime.datetime.strptime(tiemposalida, '%Y-%m-%d %H:%M:%S')
        self.tipoEspacio = tipoespacio

    def set_asignacion(self, nombreMateria, profesor, edifcio, nombreespacio):
        self.materia.set_nombreMateria(nombreMateria)
        self.materia.set_profesor(profesor)
        if (self.tipoEspacio == 'Salon'):
            self.salon.set_edificio(edifcio)
            self.salon.set_nombre(nombreespacio)
        else:
            self.lab.set_nombre(nombreespacio)
            self.lab.set_edificio(edifcio)

    def get_codigo(self):
        return self.codigo

    def get_tiempoentrada(self):
        return self.tiempoentrada

    def get_horaentrada(self):
        hora = datetime.datetime.strftime(self.tiempoentrada, "%X")
        return hora

    def get_horasalida(self):
        hora = datetime.datetime.strftime(self.tiemposalida, "%X")
        return hora

    def get_tiemposalida(self):
        return self.tiemposalida

    def set_tiempoentrada(self, x):
        self.tiempoentrada = x

    def settiemposalida(self, x):
        self.tiemposalida = x

    def crearasignacion(self):
        flagsalon = True
        self.cur.execute("SELECT nombreEspacio,horaEntrada,horaSalida FROM Asignacion")
        for (nombreEspacio, horaEntrada, horaSalida) in self.cur:
            if self.salon.get_nombre() == nombreEspacio and (
                    horaEntrada <= self.tiempoentrada <= horaSalida or horaEntrada <= self.tiemposalida <= horaSalida):
                flagsalon = False
        if flagsalon:
            self.cur.execute(
                "INSERT INTO Asignacion (nombreMateria, nombreEspacio, profesor, edificio, horaEntrada, horaSalida,TipoEspacio) VALUES (?,?,?,?,?,?,?)",
                (self.materia.get_nombreMateria(), self.salon.get_nombre(), self.materia.get_profesor(),
                 self.salon.get_edificio(), self.tiempoentrada, self.tiemposalida, self.tipoEspacio))
            self.conn.commit()
            print("La asignacion ha sido realizada con los siguientes parametros: \n" +
                  "Salon: " + self.salon.get_nombre() + "\n" +
                  "Materia: " + self.materia.get_nombreMateria() + "\n" +
                  "Hora Entrada: " + self.get_horaentrada() + "\n" +
                  "Hora Salida: " + self.get_horasalida())
        else:
            print("Asignacion fallida")

    def eliminarasignacionmateria(self, parametro, seleccion):
        self.cur.execute("SELECT nombreMateria,nombreEspacio,horaEntrada,horaSalida FROM Asignacion")
        for (nombreMateria, nombreEspacio, horaEntrada, horaSalida) in self.cur:
            print(str(nombreMateria) + " " + str(nombreEspacio) + " ")
            if seleccion == 1:
                if parametro == nombreMateria:
                    # self.cur.execute("SELECT nombreMateria FROM Asignacion")
                    self.cur.execute("DELETE FROM Asignacion WHERE  nombreMateria=?", (parametro,))
                    self.conn.commit()
                    break
            elif seleccion == 2:
                if parametro == nombreMateria:
                    # self.cur.execute("SELECT nombreMateria FROM Asignacion")
                    self.cur.execute("DELETE FROM Asignacion WHERE  nombreMateria=?", (parametro,))
                    self.conn.commit()
                    break
            else:
                break
