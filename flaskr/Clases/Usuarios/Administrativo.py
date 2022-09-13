from flask import Blueprint, render_template, request, redirect, session, flash

from Clases.Usuarios.Estudiante import Estudiante
from Clases.Usuarios.usuarios import Usuario
from Clases.Asignaciones.asignacionClase import AsignacionClase
from Metodos.DBConnection import connection
from Metodos.interfaces import VerAsignacion, CrearAsignacion, ModificarAsignacion, EliminarAsignacion


class Administrativo(Usuario, VerAsignacion,CrearAsignacion,ModificarAsignacion,EliminarAsignacion):

    bpadmin = Blueprint('adminview',__name__,url_prefix='/administrativo')

    def verasignacion(self, parametro):
        resultfinal = []
        conn = connection()
        cur = conn.cursor()
        cur.execute("select codigo,nombreMateria, nombreEspacio, profesor,edificio, horaEntrada, horaSalida from Asignacion")
        for (codigo,nombreMateria, nombreEspacio, profesor, edificio, horaEntrada, horaSalida) in cur:
            if str (codigo) in parametro or nombreMateria in parametro or parametro == nombreEspacio or parametro == profesor or parametro == edificio:
                text = "Codigo: " + str(
                    codigo) + " Materia: " + nombreMateria + " Salon: " + nombreEspacio + " Profesor: " + profesor + " " + edificio + " Fecha de entrada: " + str(
                    horaEntrada) + " Fecha Salida:  " + str(horaSalida)
                resultfinal.append(text)
        return resultfinal


    @bpadmin.route('/',methods=('GET', 'POST'))
    def __versaignacion():
        if request.method == 'GET':
            return render_template('admintemplate.html')
        else:
            param = request.form['valor']
            admin = Administrativo()
            results = admin.verasignacion(param)
            session['results'] = results
            if request.form["seleccion"] == "1":
                pass
            elif request.form["seleccion"] == "2":
                return redirect('/administrativo/eliminarasignacion')
            elif request.form["crear"] == "3":
                return  redirect('/administrativo/crearasignacion')
            else:
                flash("La busqueda no fue exitosa","error")
                return render_template("admintemplate.html")
        return render_template("admintemplate.html")


    @bpadmin.route('/eliminarasignacion', methods =('GET','POST'))
    def __eliminarAsignacion():
        if request.method == 'GET':
            results = session.get('results',None)
            return render_template("eliminartemplate.html",resultend =results)
        else:
            admin = Administrativo()
            result = admin.eliminarasignacion(int(request.form["codigo"]))
            if result:
                flash("La eliminacion fue exitosa","message")
                return redirect("/administrativo")
            else:
                flash("el codigo no es correcto","error")
                return redirect("/administrativo")







    def eliminarasignacion(self,codigoentrada):
        conn = connection()
        cur = conn.cursor()
        cur.execute("SELECT codigo FROM Asignacion")
        for (codigo) in cur:
            if codigo[0] == codigoentrada:
                cur.execute("DELETE FROM Asignacion WHERE  Codigo=?", (codigo[0],))
                conn.commit()
                return True






    def crearasignacion(self, nombreMateria, profesor, edifcio, nombreespacio, tiempoentrada,
                        tiemposalida, tipoespacio):
        asignacion = AsignacionClase()
        asignacion.set_asignacion(nombreMateria, profesor ,edifcio ,nombreespacio,tiempoentrada,tiemposalida,tipoespacio)
        return asignacion.crearasignacion()


    @bpadmin.route('/crearasignacion', methods =('GET','POST'))
    def __crearAsignacion():
        if request.method == 'POST':
            materia = request.form['materia']
            edificio = request.form['edificio']
            profesor= request.form['profesor']
            espacio = request.form['espacio']
            tiempo_entrada = request.form['tiempoentrada']
            tiempo_salida =request.form['tiemposalida']
            tipo_espacio = int(request.form['tipoespacio'])
            admin = Administrativo()
            result = admin.crearasignacion(materia,profesor,edificio,espacio,tiempo_entrada,tiempo_salida,tipo_espacio)
            if len(result) != 0:
                flash("Asignacion creada satisfactoriamente","message")
                return redirect('/administrativo/crearasignacion')
            else:
                flash('La asignacion no pudo ser creada',"error")
                return redirect('/administrativo/crearasignacion')
        else:return render_template('createasignaicontemplate.html')




    def modificarasignacion(self):
        pass






