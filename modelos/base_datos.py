import pymysql

CONFIG_BD = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "rentacar_seguro",
    "cursorclass": pymysql.cursors.DictCursor,
}


class ConexionBaseDatos:
    def __init__(self, configuracion: dict):
        self.configuracion = configuracion
        self.conexion = None

    def conectar(self):
        if self.conexion is None or not self.conexion.open:
            self.conexion = pymysql.connect(**self.configuracion)

    def ejecutar(self, consulta, parametros=None, obtener_uno=False, obtener_todos=False, confirmar=False):
        try:
            self.conectar()
            with self.conexion.cursor() as cursor:
                cursor.execute(consulta, parametros or ())
                if confirmar:
                    self.conexion.commit()
                if obtener_uno:
                    return cursor.fetchone()
                if obtener_todos:
                    return cursor.fetchall()
                return cursor.rowcount
        except Exception as error:
            print(f"[ERROR BD] {error}")
            if self.conexion:
                self.conexion.rollback()
            return None

    def cerrar(self):
        if self.conexion and self.conexion.open:
            self.conexion.close()
            self.conexion = None


base_datos = ConexionBaseDatos(CONFIG_BD)
