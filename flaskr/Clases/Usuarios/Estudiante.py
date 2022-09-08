from flask import Blueprint, request, render_template
from Clases.Asignaciones.asignacionClase import AsignacionClase



class Estudiante ():

    bpestudiante = Blueprint('estudianteview',__name__,url_prefix='/estudiante')
    def verasignacion(self,parametro,columna):
        asignacion = AsignacionClase()
        asignacion.set_parametro(parametro)
        return asignacion.verasignacion(columna)

    @bpestudiante.route('/',methods=('GET', 'POST'))
    def verasignacionwebapp():
        if request.method == 'GET':
            return render_template('estudiantetemplate.html')
        else:
            param = request.form['valor']
            columna = request.form['searh_parameter']
            est= Estudiante()
            results = est.verasignacion(param,columna)
        return render_template("estudiantetemplate.html",resultend = results)


