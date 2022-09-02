from Clases.asignacion import Asignacion
from Clases.materias import Materia
from Clases.salon import Salon



def run_test():


    edifcio = "A"
    nombreespacio = "201"
    nombreMateria = "Programacion"
    tiempoentrada = '2022-09-01 15:30:00'
    tiemposalida = '2022-09-01 18:30:01'
    profesor = "Cesar Torres"

    materia = Materia()
    salon = Salon()

    asignacion = Asignacion(1541, materia, salon,tiempoentrada=tiempoentrada,tiemposalida=tiemposalida)
    asignacion.set_asignacion(nombreMateria, profesor, edifcio, nombreespacio)
    asignacion.crearasignacion()



run_test()
