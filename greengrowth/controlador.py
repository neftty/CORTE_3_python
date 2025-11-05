from tkinter import messagebox

class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista 

    def manejar_login(self, usuario, contraseña):
        if not usuario or not contraseña:
            self.vista.mostrar_mensaje("Error de Login", "Usuario y contraseña no pueden estar vacíos.", "error")
            return
        
        if self.modelo.verificar_usuario(usuario, contraseña):
            self.vista.mostrar_mensaje("Login Exitoso", f"Bienvenido, {usuario}!")
            self.vista.mostrar_frame("FramePrincipal")
        else:
            self.vista.mostrar_mensaje("Error de Login", "Usuario o contraseña incorrectos.", "error")

    def manejar_guardar_invernadero(self, datos):
        if not datos['nombre'] or not datos['superficie']:
            self.vista.mostrar_mensaje("Error de Registro", "Nombre y Superficie son campos obligatorios.", "warning")
            return
            
        exito, mensaje = self.modelo.agregar_invernadero(datos)
        
        if exito:
            self.vista.mostrar_mensaje("Registro Exitoso", mensaje)
            self.vista.mostrar_frame("FramePrincipal") 
        else:
            self.vista.mostrar_mensaje("Error de Registro", mensaje, "error")

    def manejar_guardar_enfermedad(self, dict_datos):
        if not dict_datos['nombre_comun'] or not dict_datos['sintomas']:
            self.vista.mostrar_mensaje("Error de Registro", "Nombre común y Síntomas son obligatorios.", "warning")
            return

        exito, mensaje = self.modelo.agregar_enfermedad(dict_datos)

        if exito:
            self.vista.mostrar_mensaje("Registro Exitoso", mensaje)
            self.vista.mostrar_frame("FramePrincipal")
        else:
            self.vista.mostrar_mensaje("Error de Registro", mensaje, "error")

    def manejar_cargar_control_invernaderos(self):
        datos, mensaje = self.modelo.obtener_invernaderos()
        if datos:
            self.vista.actualizar_frame_control(datos) 
        else:
            self.vista.actualizar_frame_control([])
            if mensaje and mensaje != "Datos cargados con éxito.":
                 self.vista.mostrar_mensaje("Error de Carga", mensaje, "error")

    def manejar_cambio_estado(self, id_inv, estado):
        exito, mensaje = self.modelo.actualizar_estado_invernadero(id_inv, estado)
        
        if exito:
            self.manejar_cargar_control_invernaderos() 
        else:
            self.vista.mostrar_mensaje("Error de Actualización", mensaje, "error")

    def manejar_accion_control(self, id_inv, accion):
        
        if accion == "eliminar":
            if messagebox.askyesno("Confirmar Eliminación", f"¿Estás seguro de que quieres eliminar el invernadero ID {id_inv}?"):
                exito, mensaje = self.modelo.eliminar_invernadero(id_inv)
                if exito:
                    self.vista.mostrar_mensaje("Eliminación Exitosa", mensaje)
                    self.manejar_cargar_control_invernaderos() 
                else:
                    self.vista.mostrar_mensaje("Error", mensaje, "error")
        
        elif accion == "detalle":
            detalles, mensaje = self.modelo.obtener_detalles_invernadero(id_inv)
            if detalles:
                texto_detalles = (
                    f"ID: {detalles.get('id', 'N/A')}\n"
                    f"Nombre: {detalles.get('nombre', 'N/A')}\n"
                    f"Responsable: {detalles.get('responsable', 'N/A')}\n"
                    f"Superficie (m²): {detalles.get('superficie', 'N/A')}\n"
                    f"Tipo de cultivo: {detalles.get('tipo_cultivo', 'N/A')}\n"
                    f"Fecha de Creación: {detalles.get('fecha_creacion', 'N/A')}\n"
                    f"Capacidad Prod.: {detalles.get('capacidad_produccion', 'N/A')}\n"
                    f"Sistema de Riego: {detalles.get('sistema_riego', 'N/A')}\n"
                    f"Estado Actual: {detalles.get('estado', 'N/A')}"
                )
                self.vista.mostrar_mensaje(f"Detalles del Invernadero ID {id_inv}", texto_detalles, tipo="info")
            else:
                self.vista.mostrar_mensaje("Error", mensaje, "error")
                
        elif accion == "editar":
            detalles, mensaje = self.modelo.obtener_detalles_invernadero(id_inv)
            if detalles:
                marco_edicion = self.vista.marcos["FrameEditarInvernadero"]
                marco_edicion.cargar_datos(detalles)
                self.vista.mostrar_frame("FrameEditarInvernadero")
            else:
                self.vista.mostrar_mensaje("Error", mensaje, "error")
        
    def manejar_guardar_edicion_invernadero(self, datos):
        
        if not datos.get('nombre') or not datos.get('superficie') or not datos.get('id'):
            self.vista.mostrar_mensaje("Error de Edición", "ID, Nombre y Superficie son obligatorios.", "warning")
            return
            
        exito, mensaje = self.modelo.actualizar_invernadero(datos)
        
        if exito:
            self.vista.mostrar_mensaje("Edición Exitosa", mensaje)
            self.vista.mostrar_frame("FrameControlInvernadero") 
        else:
            self.vista.mostrar_mensaje("Error de Edición", mensaje, "error")