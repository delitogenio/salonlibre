import logging

from flask import Blueprint, render_template, request, flash, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from Clases.Usuarios.Estudiante import Estudiante
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
                        return '/administrativo'
                    elif self.tipo_usuario == 2:
                        return '/estudiante'
                    elif self.tipo_usuario == 3:
                        return 'profesortemplate.html'
                    else:
                        return '14'
        return '14'
    @bplogin.route('/', methods=('GET', 'POST'))
    def __login():
        logging.info(request.url + ' ' + request.method)
        if request.method == 'POST':
            login = Login()
            result = login.login()
            if result == '14':
                flash('Credenciales no validas', 'error')
                return render_template('login.html')
            else:return redirect(result)
        else:
            return render_template('login.html')
    def create_login(self):
        flag = True
        conn = connection()
        cur = conn.cursor()
        self.nombreUsuario = request.form["user"]
        self.contrasena = request.form["password"]
        cur.execute("Select * from Tipos_Usuario")
        for Correo_Institucional,Tipo_Usuario in cur:
            if self.nombreUsuario == Correo_Institucional:
                self.tipo_usuario = Tipo_Usuario
                flag =True
                break
            else: flag  = False

        rta_pregunta1 = request.form["pregunta1"]
        rta_pregunta2 = request.form["pregunta2"]
        rta_pregunta3 = request.form["pregunta3"]

        cur.execute("SELECT Usuario,Contrasena FROM Usuarios")
        for Usuario, Contrasena in cur:
            if Usuario == self.nombreUsuario:
                session['error_usuario_creado'] = 'El usuario ya esta creado en el sistema'
                return False
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
            session['error_usuario_creado'] = None
            flash('Usuario creado correctamente', 'message')
            return True

    @bplogin.route('/createlogin', methods=('GET', 'POST'))
    def __create_login():
        if request.method == 'GET':
            return render_template('logincreation.html')
        else:
            login = Login()
            bol = login.create_login()
            message = session.get('error_usuario_creado')
            if bol and message == None:
                return redirect('/login')
            elif message  == 'El usuario ya esta creado en el sistema':
                flash('El usuario ya esta creado en el sistema', 'error')
                session['error_usuario_creado'] = None
                return redirect('/login/createlogin')
            else:
                flash('El correo no se encuentra en la base de datos','error')
                return redirect('/login/createlogin')

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
        logging.info(request.url + ' ' + request.method)
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
        logging.info(request.url + ' ' + request.method)
        if request.method == 'POST':
            login = Login()
            result = login.reset_password()
            return redirect(result)
        else:
            return render_template('newpasswordset.html')


