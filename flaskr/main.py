from flaskr.Clases.asignacion import Asignacion
from flaskr.Clases.materias import Materia
from flaskr.Clases.salon import Salon
from flask import Flask, render_template, request
import os
import logging, logging.config
logging.basicConfig(level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s',
                    handlers=[
                        logging.FileHandler('extractdata.log'),
                        logging.StreamHandler()
                    ])


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # UPLOAD_FOLDER = 'flaskr/Files'
    # ALLOWED_EXTENSIONS = {'txt', 'log', 'csv', 'xls'}
    # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    SESSION_TYPE = 'filesystem'
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    @app.route('/')
    def hello():
        logging.info(request.url + ' ' + request.method)
        return 0

    if __name__ == "__main__":
        app.run(debug=True)

    return app
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
