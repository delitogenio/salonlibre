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
                    self.tipo_usuario=int.from_bytes(Tipo_de_Usuario,"little")
                    if self.tipo_usuario == 1:
                        return 'admintemplate.html'
                    elif self.tipo_usuario == 2:
                        return' estudiantetemplate.html'
                    elif self.tipo_usuario == 3:
                        return 'profesortemplate.html'
                    else: return '14'
                else:
                    return ('14')
        else:return 'login.html'

    @bplogin.route('/login', methods=('GET', 'POST'))
    def __login():
        login = Login()
        result =login.login()
        if result != '14':
            return render_template(result)
        else:
            flash('Credenciales no validas','error')
            return redirect ('/login/login')







    def create_login(self,tipo_usuario):
        conn = connection()
        cur = conn.cursor()
        flag =True
        cur.execute("SELECT Usuario,Contrasena FROM Usuarios")
        for Usuario, Contrasena in cur:
            if Usuario == self.nombreUsuario:
                print("El usuario ya esta creado")
                flag=False
        if flag:
            cur.execute("INSERT INTO Usuarios(Usuario, Contrasena, Tipo_de_Usuario) VALUES (?,?,?)",(self.nombreUsuario, self.contrasena, tipo_usuario,))
            conn.commit()


















