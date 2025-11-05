import mysql.connector
from mysql.connector import Error
from gestor_base_datos import conectar 

class Modelo:
   
    def __init__(self):
        self.conexion = conectar()

    def verificar_usuario(self, usuario, contraseña):
        if not self.conexion or not self.conexion.is_connected():
            self.conexion = conectar()
            if not self.conexion:
                return False

        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT COUNT(*) FROM usuarios WHERE usuario = %s AND contraseña = %s"
            valores = (usuario, contraseña)
            cursor.execute(consulta, valores)
            (conteo,) = cursor.fetchone()
            cursor.close()
            return conteo == 1
        except Error as error:
            print(f"Error al verificar usuario: {error}")
            return False

    def agregar_invernadero(self, datos):
        if not self.conexion or not self.conexion.is_connected():
            self.conexion = conectar()
            if not self.conexion:
                return False, "Error: No se pudo conectar a la base de datos."
        try:
            cursor = self.conexion.cursor()
            consulta = """
            INSERT INTO invernaderos 
            (nombre, superficie, tipo_cultivo, fecha_creacion, responsable, capacidad_produccion, sistema_riego, estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (datos['nombre'], datos['superficie'], datos['tipo_cultivo'], datos['fecha_creacion'], 
                      datos['responsable'], datos['capacidad_produccion'], datos['sistema_riego'], 'Operativo')
            cursor.execute(consulta, valores)
            self.conexion.commit()
            cursor.close()
            return True, "Invernadero registrado con éxito."
        except Error as error:
            print(f"Error al insertar invernadero: {error}")
            return False, f"Error al registrar: {error}"

    def obtener_invernaderos(self):
        if not self.conexion or not self.conexion.is_connected():
            self.conexion = conectar()
            if not self.conexion:
                return [], "Error: No se pudo conectar a la base de datos."

        try:
            cursor = self.conexion.cursor(dictionary=True) 
            consulta = "SELECT id, nombre, estado FROM invernaderos" 
            cursor.execute(consulta)
            datos = cursor.fetchall()
            cursor.close()
            return datos, "Datos cargados con éxito."
        except Error as error:
            print(f"Error al obtener invernaderos: {error}")
            return [], f"Error al obtener datos: {error}"

    def obtener_detalles_invernadero(self, id_inv):
        if not self.conexion or not self.conexion.is_connected():
            self.conexion = conectar()
            if not self.conexion:
                return None, "Error: No se pudo conectar a la base de datos."
        
        try:
            cursor = self.conexion.cursor(dictionary=True)
            consulta = "SELECT * FROM invernaderos WHERE id = %s"
            cursor.execute(consulta, (id_inv,))
            detalles = cursor.fetchone()
            cursor.close()
            
            if detalles:
                return detalles, "Detalles cargados con éxito."
            else:
                return None, f"Invernadero ID {id_inv} no encontrado."
                
        except Error as error:
            print(f"Error al obtener detalles: {error}")
            return None, f"Error al cargar detalles: {error}"
            
    def actualizar_estado_invernadero(self, id_inv, estado):
        if not self.conexion or not self.conexion.is_connected():
            self.conexion = conectar()
            if not self.conexion:
                return False, "Error: No se pudo conectar a la base de datos."

        try:
            cursor = self.conexion.cursor()
            consulta = "UPDATE invernaderos SET estado = %s WHERE id = %s"
            cursor.execute(consulta, (estado, id_inv))
            self.conexion.commit()
            cursor.close()
            if cursor.rowcount == 0:
                return False, f"Invernadero ID {id_inv} no encontrado."
            return True, f"Estado del Invernadero ID {id_inv} actualizado a '{estado}' con éxito."
        except Error as error:
            print(f"Error al actualizar estado: {error}")
            return False, f"Error al actualizar estado: {error}"
            
    def actualizar_invernadero(self, datos):
        if not self.conexion or not self.conexion.is_connected():
            self.conexion = conectar()
            if not self.conexion:
                return False, "Error: No se pudo conectar a la base de datos."

        try:
            cursor = self.conexion.cursor()
            consulta = """
            UPDATE invernaderos SET 
                nombre = %s, 
                superficie = %s, 
                tipo_cultivo = %s, 
                fecha_creacion = %s, 
                responsable = %s, 
                capacidad_produccion = %s, 
                sistema_riego = %s
            WHERE id = %s
            """
            valores = (
                datos['nombre'], datos['superficie'], datos['tipo_cultivo'], datos['fecha_creacion'], 
                datos['responsable'], datos['capacidad_produccion'], datos['sistema_riego'], 
                datos['id'] 
            )
            cursor.execute(consulta, valores)
            self.conexion.commit()
            cursor.close()
            if cursor.rowcount == 0:
                return False, f"Invernadero ID {datos['id']} no encontrado para actualizar."
            return True, f"Invernadero ID {datos['id']} actualizado con éxito."
        except Error as error:
            print(f"Error al actualizar invernadero: {error}")
            return False, f"Error al actualizar: {error}"

    def eliminar_invernadero(self, id_inv):
        if not self.conexion or not self.conexion.is_connected():
            self.conexion = conectar()
            if not self.conexion:
                return False, "Error: No se pudo conectar a la base de datos para eliminar."

        try:
            cursor = self.conexion.cursor()
            consulta = "DELETE FROM invernaderos WHERE id = %s"
            cursor.execute(consulta, (id_inv,))
            self.conexion.commit()
            cursor.close()
            if cursor.rowcount == 0:
                return False, f"Invernadero ID {id_inv} no encontrado."
            return True, f"Invernadero ID {id_inv} eliminado con éxito."
        except Error as error:
            print(f"Error al eliminar invernadero: {error}")
            return False, f"Error al eliminar: {error}"

    def agregar_enfermedad(self, dict_datos):
        if not self.conexion or not self.conexion.is_connected():
            self.conexion = conectar()
            if not self.conexion:
                return False, "Error: No se pudo conectar a la base de datos."

        try:
            cursor = self.conexion.cursor()
            consulta = """
            INSERT INTO enfermedades 
            (nombre_comun, nombre_cientifico, sintomas, tratamiento)
            VALUES (%s, %s, %s, %s)
            """
            valores = (
                dict_datos['nombre_comun'],
                dict_datos['nombre_cientifico'],
                dict_datos['sintomas'],
                dict_datos['tratamiento']
            )
            cursor.execute(consulta, valores)
            self.conexion.commit()
            cursor.close()
            return True, "Enfermedad registrada con éxito."
        except Error as error:
            print(f"Error al insertar enfermedad: {error}")
            return False, f"Error al registrar: {error}"

    def __del__(self):
        if hasattr(self, 'conexion') and self.conexion and self.conexion.is_connected():
            self.conexion.close()
            print("Conexión a la base de datos cerrada.")