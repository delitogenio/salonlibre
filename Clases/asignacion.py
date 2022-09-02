import datetime
from Metodos.DBConnection import connection

from Clases.materias import Materia
from Clases.salon import Salon


class Asignacion():
    codigo = None
    materia = Materia()
    salon = Salon()
    tiempoentrada = None
    tiemposalida = None
    cur = connection()

    def __init__(self, codigo, materia, salon, tiempoentrada, tiemposalida):
        self.codigo = codigo
        self.materia = materia
        self.salon = salon
        self.tiempoentrada = datetime.datetime.strptime(tiempoentrada, '%Y-%m-%d %H:%M:%S')
        self.tiemposalida = datetime.datetime.strptime(tiemposalida, '%Y-%m-%d %H:%M:%S')

    def set_asignacion(self, nombreMateria, profesor, edifcio, nombreespacio):
        self.materia.set_nombreMateria(nombreMateria)
        self.materia.set_profesor(profesor)
        self.salon.set_edificio(edifcio)
        self.salon.set_nombre(nombreespacio)

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
        for (nombreEspacio,horaEntrada,horaSalida) in self.cur:
            if nombreEspacio[0] == self.salon.get_nombre() or horaEntrada <= self.tiempoentrada <= horaSalida or horaEntrada <= self.tiemposalida<= horaSalida:
                flagsalon=False
        self.cur._clear_result()
        if flagsalon:
            self.cur.execute("INSERT INTO `ProgIDB`.`Asignacion` (`nombreMateria`, `nombreEspacio`, `profesor`, `edificio`, `horaEntrada`, `horaSalida`) VALUES (?, ?,?,?,?,?)",(
                self.materia.get_nombreMateria(),self.materia.get_profesor(),self.salon.get_nombre(),
                self.salon.get_edificio(),self.tiempoentrada,self.tiemposalida))
        else: print("Asignacion fallida")
















