from Clases.asignacion import Asignacion
from Clases.materias import Materia
from Clases.salon import Salon



def run_test():


    edifcio = 'B'
    nombreespacio = '210'
    nombreMateria = 'Ingenieria de Software'
    tiempoentrada = '2022-09-03 15:20:59'
    tiemposalida = '2022-09-03 17:30:04'
    profesor = 'Fernando Velazco'
    tipoEspacio = 'Salon'

    materia = Materia()
    salon = Salon()

    asignacion = Asignacion(1541, materia, salon, tiempoentrada, tiemposalida,tipoEspacio)
    asignacion.set_asignacion(nombreMateria, profesor, edifcio, nombreespacio)
    # asignacion.crearasignacion()
    # asignacion.eliminarasignacionmateria("Programacion")



run_test()
