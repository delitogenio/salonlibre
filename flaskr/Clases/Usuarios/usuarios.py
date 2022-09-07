#defincion y creacion de los usuarios
import abc
from Metodos.Login import Login
from Metodos.DBConnection import connection


class Usuario(abc.ABC):
    correo=None
    contrasena=None
    tipousuario = None






