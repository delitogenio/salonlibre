import logging

import requests
from flask import Blueprint, render_template, request, flash, redirect

from Metodos.DBConnection import connection




class Login:

    nombreUsuario=None
    contrasena = None
    tipo_usuario=0
    bplogin = Blueprint('login', __name__, url_prefix='/login')
    def login(self):
        logging.info(request.url + ' ' + request.method)
        if request.method == 'POST':
            conn = connection()
            cur = conn.cursor()
            cur.execute("SELECT Usuario,Contrasena,Tipo_de_Usuario FROM Usuarios")
            self.nombreUsuario = request.form["user"]
            self.contrasena = request.form["password"]
            for Usuario, Contrasena,Tipo_de_Usuario in cur:
                if Usuario == self.nombreUsuario and Contrasena == self.contrasena:
                    self.tipo_usuario=Tipo_de_Usuario
                    if self.tipo_usuario == 1:
                        return 'admintemplate.html'
                    elif self.tipo_usuario == 2:
                        return' estudiantetemplate.html'
                    elif self.tipo_usuario == 3:
                        return 'profesortemplate.html'
                    else: return '14'
        else:return 'login.html'

    @bplogin.route('/', methods=('GET', 'POST'))
    def __login():

        login = Login()
        result =login.login()
        if result != '14':
            return render_template(result)
        else:
            flash('Credenciales no validas','error')
            return redirect ('/login')
    def create_login(self,tipo_usuario):
        self.nombreUsuario = request.form["user"]
        self.contrasena = request.form["password"]
        self.tipo_usuario = int(tipo_usuario)
        conn = connection()
        cur = conn.cursor()
        flag =True
        cur.execute("SELECT Usuario,Contrasena FROM Usuarios")
        for Usuario, Contrasena in cur:
            if Usuario == self.nombreUsuario:
                flag=False
                return flash('El usuario ya esta creado','error')
        if flag:
            cur.execute("INSERT INTO Usuarios(Usuario, Contrasena, Tipo_de_Usuario) VALUES (?,?,?)",(self.nombreUsuario, self.contrasena, self.tipo_usuario,))
            conn.commit()
            flash('Usuario creado correctamente','message')


    @bplogin.route('/createlogin', methods=('GET', 'POST'))
    def __create_login ():
        if request.method == 'GET':
            return render_template('logincreation.html')
        else:
            login = Login()
            login.create_login(request.form['lista_tipos_usuario'])
            return redirect('/login')


















