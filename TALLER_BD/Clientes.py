from Gestor_base_datos import conectar
from mysql.connector import Error

class Clientes: 
    def __init__(self):
        self.conexion = conectar()

    def agregarCliente(self, idCliente, nombre, apellido, email, historial):
        if not self.conexion:
            print("No hay conexión con la base de datos.")
            return
        
        cursor = None
        try:
            cursor = self.conexion.cursor()
            sql = """
                INSERT INTO clientes (idCliente, nombreCliente, apellidoCliente, emailCliente, historialCliente)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (idCliente, nombre, apellido, email, historial))
            
            self.conexion.commit()
            print("Cliente agregado correctamente.")
        except Error as e:
            print(f"Error al agregar cliente: {e}")
            self.conexion.rollback() 
        finally:
            if cursor:
                cursor.close()

    def consultarClientes(self):
        if not self.conexion:
            return []
        
        cursor = None
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM clientes")
            datos = cursor.fetchall()
            print("Consulta de clientes exitosa.")
            return datos
        except Error as e:
            print(f"Error al consultar clientes: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def actualizarCliente(self, idCliente, nombre, apellido, email, historial):
        if not self.conexion:
            return
        
        cursor = None
        try:
            cursor = self.conexion.cursor()
            sql = """
                UPDATE clientes
                SET nombreCliente=%s, apellidoCliente=%s, emailCliente=%s, historialCliente=%s
                WHERE idCliente=%s
            """
            cursor.execute(sql, (nombre, apellido, email, historial, idCliente))
            self.conexion.commit()
            print("Cliente actualizado correctamente.")
        except Error as e:
            print(f"Error al actualizar cliente: {e}")
            self.conexion.rollback() 
        finally:
            if cursor:
                cursor.close()

    def eliminarCliente(self, idCliente):
        if not self.conexion:
            return
        
        cursor = None
        try:
            cursor = self.conexion.cursor()
            sql = "DELETE FROM clientes WHERE idCliente=%s"
            cursor.execute(sql, (idCliente,))
            self.conexion.commit()
            print("Cliente eliminado correctamente.")
        except Error as e:
            print(f"Error al eliminar cliente: {e}")
            self.conexion.rollback() 
        finally:
            if cursor:
                cursor.close()

    def totalComprasPorCliente(self):
        if not self.conexion:
            return []
        
        cursor = None
        try:
            cursor = self.conexion.cursor()
            sql = """
                SELECT nombreCliente, apellidoCliente, SUM(historialCliente) 
                FROM clientes 
                GROUP BY nombreCliente, apellidoCliente
            """
            cursor.execute(sql)
            return cursor.fetchall()
        except Error as e:
            print(f"Error al calcular total de compras: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def valorTotalCompras(self):
        if not self.conexion:
            return 0
        
        cursor = None
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT SUM(historialCliente) FROM clientes")
            total = cursor.fetchone()[0]
            return total if total else 0
        except Error as e:
            print(f" Error al calcular valor total: {e}")
            return 0
        finally:
            if cursor:
                cursor.close()