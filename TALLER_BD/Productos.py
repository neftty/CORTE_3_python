from Gestor_base_datos import conectar
from mysql.connector import Error

class Productos:  
    def __init__(self):
        self.conexion = conectar()
        
    def agregarProducto(self, idProducto, nombreProducto, precioProducto, stockProducto, categoriaProducto):
        if not self.conexion:
            print("No hay conexión con la base de datos.")
            return
        
        cursor = None 
        try:
            cursor = self.conexion.cursor()
            
            sql = """
                INSERT INTO productos (idProducto, nombreProducto, precioProducto, stockProducto, categoriaProducto)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (idProducto, nombreProducto, precioProducto, stockProducto, categoriaProducto))
            
            self.conexion.commit()
            print("Producto agregado correctamente.")
        except Error as e:
            print(f"Error al agregar producto: {e}")
            self.conexion.rollback() 
        finally:
            if cursor:
                cursor.close()

    def consultarProductos(self):
        if not self.conexion:
            return []
        
        cursor = None
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM productos")
            datos = cursor.fetchall()
            print("Consulta de productos exitosa.")
            return datos
        except Error as e:
            print(f"Error al consultar productos: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def actualizarProducto(self, idProducto, nombre, precio, stock, categoria):
        if not self.conexion:
            return
        
        cursor = None
        try:
            cursor = self.conexion.cursor()
            sql = """
                UPDATE productos
                SET nombreProducto=%s, precioProducto=%s, stockProducto=%s, categoriaProducto=%s
                WHERE idProducto=%s
            """
            cursor.execute(sql, (nombre, precio, stock, categoria, idProducto))
            self.conexion.commit()
            print("Producto actualizado correctamente.")
        except Error as e:
            print(f"Error al actualizar producto: {e}")
            self.conexion.rollback() 
        finally:
            if cursor:
                cursor.close()

    def eliminarProducto(self, idProducto):
        if not self.conexion:
            return
        
        cursor = None
        try:
            cursor = self.conexion.cursor()
            sql = "DELETE FROM productos WHERE idProducto=%s"
            cursor.execute(sql, (idProducto,))
            self.conexion.commit()
            print("Producto eliminado correctamente.")
        except Error as e:
            print(f"Error al eliminar producto: {e}")
            self.conexion.rollback() 
        finally:
            if cursor:
                cursor.close()

    def valorPorCategoria(self):
        if not self.conexion:
            return []
        
        cursor = None
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT categoriaProducto, SUM(precioProducto * stockProducto) FROM productos GROUP BY categoriaProducto")
            return cursor.fetchall()
        except Error as e:
            print(f"Error al calcular valor por categoría: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def valorTotalInventario(self):
        if not self.conexion:
            return 0
        
        cursor = None
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT SUM(precioProducto * stockProducto) FROM productos")
            total = cursor.fetchone()[0]
            return total if total else 0
        except Error as e:
            print(f"Error al calcular inventario total: {e}")
            return 0
        finally:
            if cursor:
                cursor.close()

    def productosStockBajo(self, limite=5):
        if not self.conexion:
            return []
        
        cursor = None
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM productos WHERE stockProducto < %s", (limite,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error al consultar productos con poco stock: {e}")
            return []
        finally:
            if cursor:
                cursor.close()