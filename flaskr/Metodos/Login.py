from Metodos.DBConnection import connection


class Login:

    nombreUsuario=None
    contrasena = None
    tipo_usuario=None

    def __init__(self, usuario, contrasena):
        self.nombreUsuario=usuario
        self.contrasena=contrasena

    def login(self):
        conn = connection()
        cur = conn.cursor()
        cur.execute("SELECT Usuario,Contrasena FROM Usuarios")
        for Usuario, Contrasena in cur:
            if Usuario == self.nombreUsuario and Contrasena == self.contrasena:
                print("Login Successfull")
            else:
                print("Credenciales Incorrectas")
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

















log = Login("cbetancur@emida.net","654987123")
log.create_login("Administrativo")












