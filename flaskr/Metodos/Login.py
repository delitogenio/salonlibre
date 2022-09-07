import logging
from werkzeug.security import generate_password_hash, check_password_hash
import requests
from flask import Blueprint, render_template, request, flash, redirect, session

from Metodos.DBConnection import connection


class Login:
    nombreUsuario = None
    contrasena = None
    tipo_usuario = 0
    bplogin = Blueprint('login', __name__, url_prefix='/login')

    def login(self):
        logging.info(request.url + ' ' + request.method)
        if request.method == 'POST':
            conn = connection()
            cur = conn.cursor()
            cur.execute("SELECT Usuario,Contrasena,Tipo_de_Usuario FROM Usuarios")
            self.nombreUsuario = request.form["user"]
            self.contrasena = request.form["password"]
            for Usuario, Contrasena, Tipo_de_Usuario in cur:
                if Usuario == self.nombreUsuario and check_password_hash(Contrasena, self.contrasena):
                    self.tipo_usuario = Tipo_de_Usuario
                    if self.tipo_usuario == 1:
                        return 'admintemplate.html'
                    elif self.tipo_usuario == 2:
                        return ' estudiantetemplate.html'
                    elif self.tipo_usuario == 3:
                        return 'profesortemplate.html'
                    else:
                        return '14'
        return '14'

    @bplogin.route('/', methods=('GET', 'POST'))
    def __login():

        login = Login()
        result = login.login()
        if result == '14':
            flash('Credenciales no validas', 'error')
            return render_template('login.html')
        else:return render_template(result)



    def create_login(self, tipo_usuario):
        self.nombreUsuario = request.form["user"]
        self.contrasena = request.form["password"]
        self.tipo_usuario = int(tipo_usuario)
        rta_pregunta1 = request.form["pregunta1"]
        rta_pregunta2 = request.form["pregunta2"]
        rta_pregunta3 = request.form["pregunta3"]
        conn = connection()
        cur = conn.cursor()
        flag = True
        cur.execute("SELECT Usuario,Contrasena FROM Usuarios")
        for Usuario, Contrasena in cur:
            if Usuario == self.nombreUsuario:
                flag = False
                return flash('El usuario ya esta creado', 'error')
        if flag:
            password_encripted = generate_password_hash(self.contrasena)
            rta1_encrypted = generate_password_hash(rta_pregunta1)
            rta2_encrypted = generate_password_hash(rta_pregunta2)
            rta3_encrypted = generate_password_hash(rta_pregunta3)
            cur.execute(
                "INSERT INTO Usuarios(Usuario,Contrasena ,Tipo_de_Usuario,RTA_Seguridad_1,RTA_Seguridad_2,RTA_Seguridad_3) VALUES (?,?,?,?,?,?)",
                (self.nombreUsuario, password_encripted, self.tipo_usuario,
                 rta1_encrypted, rta2_encrypted, rta3_encrypted))
            conn.commit()
            flash('Usuario creado correctamente', 'message')

    @bplogin.route('/createlogin', methods=('GET', 'POST'))
    def __create_login():
        if request.method == 'GET':
            return render_template('logincreation.html')
        else:
            login = Login()
            login.create_login(request.form['lista_tipos_usuario'])
            return redirect('/login')

    def reset_password_initial(self):
        nombreUsuario = request.form["usuario"]
        session['usuario'] = nombreUsuario
        conn = connection()
        cur = conn.cursor()
        cur.execute("Select Usuario,RTA_Seguridad_1,RTA_Seguridad_2,RTA_Seguridad_3 from Usuarios")
        for Usuario, RTA_Seguridad_1, RTA_Seguridad_2, RTA_Seguridad_3 in cur:
            if nombreUsuario == Usuario and check_password_hash(RTA_Seguridad_1,
                                                                request.form["pregunta1"]) and check_password_hash(
                    RTA_Seguridad_2, request.form["pregunta2"]) and check_password_hash(RTA_Seguridad_3,
                                                                                        request.form["pregunta3"]):
                return '/newpasswordset'
            else:
                return '/forgotpassword'

    @bplogin.route('/forgotpassword', methods=('GET', 'POST'))
    def __reset_password_initial():
        if request.method == 'POST':
            login = Login()
            result = login.reset_password_initial()
            return redirect('/login'+result)
        else:
            return render_template("forgotpassword.html")

    def reset_password(self):
        user= session.get('usuario',None)
        newpassword = generate_password_hash(request.form["password"])
        conn = connection()
        cur = conn.cursor()
        cur.execute("Select Usuario,Contrasena from Usuarios")
        cur.execute("UPDATE Usuarios SET Contrasena =? where Usuario=?",(newpassword,user,))
        conn.commit()
        flash("Contraseña cambiada correctamente","message")
        return '/login'

    @bplogin.route('/newpasswordset', methods=('GET', 'POST'))
    def __reset_password():
        if request.method == 'POST':
            login = Login()
            result = login.reset_password()
            return redirect(result)
        else:
            return render_template('newpasswordset.html')


