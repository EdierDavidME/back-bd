from utils.DateFormat import DateFormat

class User():
    def __init__(self, ID, cedula=None, fecha_nacimiento=None,
                 nombre1=None, nombre2=None, apellido1=None,
                 apellido2=None, correo=None,
                 creado_cuenta=None, login=None, genero=None):
        self.ID = ID
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.correo = correo
        self.creado_cuenta = creado_cuenta
        self.login = login
        self.genero = genero

    def to_JSON(self):
        return {
            'ID': self.ID,
            'cedula': self.cedula,
            'fecha_nacimiento': self.fecha_nacimiento,
            'nombre1': self.nombre1,
            'nombre2': self.nombre2,
            'apellido1': self.apellido1,
            'apellido2': self.apellido2,
            'correo': self.correo,
            'creado_cuenta': self.creado_cuenta,
            'login': self.login,
            'genero': self.genero,
        }
