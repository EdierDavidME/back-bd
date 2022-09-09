from database.db import get_connection
from .entities.User import User


class UserModel():

    @classmethod
    def get_users(self):
        try:
            connection = get_connection()
            users = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT 'ID', 'cedula', 'fecha_nacimiento', 'nombre1', 'nombre2', 'apellido1', 'apellido2', 'correo', 'creado_cuenta', 'login', 'genero' FROM User")
                resultset = cursor.fetchall()

                print("::: resultset :::", resultset)
                if (len(resultset) > 0):
                    for row in resultset:
                        user = User(row[0], row[1], row[2], row[3], row[4], row[5],
                                    row[6], row[7], row[8], row[9], row[10])
                        users.append(user.to_JSON())

                connection.close()
                return users
        except Exception as ex:
            raise Exception(ex)
