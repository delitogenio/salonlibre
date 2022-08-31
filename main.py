from Metodos.asignacion import Asignacion
from Clases.materias import Materia
from Clases.salon import Salon


def run_test():
    edifcio = '201'
    nombreespacio = 'Harwdare Libre'
    nombreMateria = 'POO'
    tiempoentrada = '2022-08-26 18:00:00'
    tiemposalida = '2022-08-26 20:00:00'
    profesor = 'Cesar Torres'

    materia = Materia()
    salon = Salon()

    asignacion = Asignacion(1541, materia, salon)
    asignacion.set_asignacion(nombreMateria, tiempoentrada, tiemposalida, profesor, edifcio, nombreespacio)
    print("El codigo de la asignacion es "+ str(asignacion.get_codigo()))
    print("La hora de entrada es "+ asignacion.materia.get_tiempoentrada())
    print("La hora de salida es " + asignacion.materia.get_tiemposalida())
    print("El profesor asignado es " + asignacion.materia.get_profesor())
    print("El salon es " + asignacion.salon.get_nombre() + " en el edificio "+ asignacion.salon.get_edificio() )


run_test()
