import mariadb

# https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/

class DaoMariaDB:
    conexion = None

    def __init__(self):
        print("Conectando con el servidor MariaDB")
        if self.conexion is None:
            try:
                self.conexion = mariadb.connect(
                    user="andyparla",
                    password="Trasto,.01",
                    host="192.168.5.59",
                    port=3306,
                    database="encrypt")
                print("Conectado...")
            except mariadb.Error as e:
                print(f"Error connecting to MariaDB Platform: {e}")

    def obtenerInfoByApp(self, id_app: str):
        # Get Cursor
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM ENCRYPT WHERE APP_NAME=?", (id_app,))
        for fila in cursor:
            print(f"ID: {fila[0]}, app_name: {fila[1]}, key: {fila[2]}, app_descripcion: {fila[3]}")
        cursor.close()
        self.conexion.close()

    def obtenerKeyByApp(self, id_app: str):
        # Get Cursor
        cursor = self.conexion.cursor()
        cursor.execute("SELECT KEY_ENCRYPT FROM ENCRYPT WHERE APP_NAME=?", (id_app,))
        data = cursor.fetchone()[0]
        cursor.close()
        self.conexion.close()
        return data
