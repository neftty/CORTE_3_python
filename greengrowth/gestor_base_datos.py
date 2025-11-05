import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexion = mysql.connector.connect(
            host = "localhost",
            database = "Invernadero",
            user = "root",
            password = ""
        )
        
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos 'Invernadero'.")
        else:
            print("Error: La conexión no se pudo establecer correctamente.")
        
        return conexion
        
    except Error as error:
        print(f"ERROR de conexión a la base de datos: {error}")
        return None