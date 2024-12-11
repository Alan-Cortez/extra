import mysql.connector
from apps.config import Config

class Usuario:
    @staticmethod
    def obtener_conexion():
        return mysql.connector.connect(
            host=Config.MYSQL_HOST,
            database=Config.MYSQL_DATABASE,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD
        )

    @staticmethod
    def crear_usuario(usuario, contrasena):
        con = Usuario.obtener_conexion()
        cursor = con.cursor()
        sql = "INSERT INTO tst0_usuarios (Nombre_Usuario, Contrasena) VALUES (%s, %s)"
        cursor.execute(sql, (usuario, contrasena))
        con.commit()
        cursor.close()
        con.close()

    @staticmethod
    def obtener_usuarios():
        con = Usuario.obtener_conexion()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM tst0_usuarios ORDER BY Id_Usuario DESC")
        registros = cursor.fetchall()
        cursor.close()
        con.close()
        return registros

    @staticmethod
    def actualizar_usuario(id_usuario, usuario, contrasena):
        con = Usuario.obtener_conexion()
        cursor = con.cursor()
        sql = "UPDATE tst0_usuarios SET Nombre_Usuario=%s, Contrasena=%s WHERE Id_Usuario=%s"
        cursor.execute(sql, (usuario, contrasena, id_usuario))
        con.commit()
        cursor.close()
        con.close()

    @staticmethod
    def eliminar_usuario(id_usuario):
        con = Usuario.obtener_conexion()
        cursor = con.cursor()
        sql = "DELETE FROM tst0_usuarios WHERE Id_Usuario=%s"
        cursor.execute(sql, (id_usuario,))
        con.commit()
        cursor.close()
        con.close()
