import tkinter as tk
from tkinter import ttk, messagebox

class FrameLogin(ttk.Frame):
    def __init__(self, padre, vista):
        super().__init__(padre, style="TFrame")
        self.vista = vista 
        
        marco = ttk.Frame(self, style="TFrame")
        marco.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(marco, text="Iniciar Sesión", style="Header.TLabel").pack(pady=20)

        ttk.Label(marco, text="Usuario", style="TLabel").pack(pady=(0, 5), anchor="w")
        self.entrada_usuario = ttk.Entry(marco, width=40, style="TEntry")
        self.entrada_usuario.pack(pady=(0, 10))

        ttk.Label(marco, text="Contraseña", style="TLabel").pack(pady=(0, 5), anchor="w")
        self.entrada_contraseña = ttk.Entry(marco, width=40, show="*", style="TEntry")
        self.entrada_contraseña.pack(pady=(0, 20))

        ttk.Button(
            marco, 
            text="Confirmar", 
            style="Green.TButton",
            command=lambda: self.vista.controlador.manejar_login(
                self.entrada_usuario.get(),
                self.entrada_contraseña.get()
            )
        ).pack(pady=10, fill="x")


class FramePrincipal(ttk.Frame):
    def __init__(self, padre, vista):
        super().__init__(padre, style="TFrame")
        self.vista = vista
        
        barra_navegacion = tk.Frame(self, bg=self.vista.accent_color)
        barra_navegacion.pack(side="top", fill="x")
        
        botones = {
            "Registrar Invernaderos": "FrameRegistroInvernadero",
            "Control Invernaderos": "FrameControlInvernadero",
            "Control de Humedad": "FrameHumedad",
            "Control de Piso": "FramePiso",
            "Enfermedades": "FrameEnfermedad"
        }
        
        for texto, nombre_frame in botones.items():
            ttk.Button(
                barra_navegacion, 
                text=texto,
                style="Nav.TButton",
                command=lambda fn=nombre_frame: self.vista.mostrar_frame(fn) if fn else None
            ).pack(side="left", padx=0, pady=0)
            
        ttk.Button(
            barra_navegacion, 
            text="Salir",
            style="NavRed.TButton",
            command=lambda: self.vista.mostrar_frame("FrameLogin")
        ).pack(side="right", padx=0, pady=0)

        marco_contenido = ttk.Frame(self, style="TFrame")
        marco_contenido.pack(fill="both", expand=True, padx=20, pady=20)
        
        marco_centrado = ttk.Frame(marco_contenido, style="TFrame")
        marco_centrado.place(relx=0.5, rely=0.4, anchor="center")

        ttk.Label(marco_centrado, text="Bienvenido a GreenGrowth S.A.", style="Header.TLabel").pack()
        ttk.Label(marco_centrado, text="Seleccione una opción del menú superior.", style="TLabel").pack(pady=10)


class FrameRegistroInvernadero(ttk.Frame):
    def __init__(self, padre, vista):
        super().__init__(padre, style="TFrame")
        self.vista = vista
        
        marco_contenido = ttk.Frame(self, style="TFrame")
        marco_contenido.pack(fill="both", expand=True, padx=40, pady=20)

        ttk.Label(marco_contenido, text="Registrar Invernadero", style="Header.TLabel").grid(row=0, column=0, columnspan=4, pady=20, sticky="w")

        campos_col1 = ["Nombre del invernadero", "Superficie (m²)", "Tipo de cultivo", "Fecha de creacion (YYYY-MM-DD)", "Responsable del invernadero"]
        self.entradas = {}
        
        for i, campo in enumerate(campos_col1):
            ttk.Label(marco_contenido, text=campo, style="TLabel").grid(row=i+1, column=0, sticky="w", pady=5, padx=10)
            entrada = ttk.Entry(marco_contenido, width=30, style="TEntry")
            entrada.grid(row=i+1, column=1, sticky="w", pady=5, padx=10)
            self.entradas[campo.split(" ")[0].lower()] = entrada 

        ttk.Label(marco_contenido, text="Capacidad de producción", style="TLabel").grid(row=1, column=2, sticky="w", pady=5, padx=10)
        entrada_cap = ttk.Entry(marco_contenido, width=30, style="TEntry")
        entrada_cap.grid(row=1, column=3, sticky="w", pady=5, padx=10)
        self.entradas['capacidad'] = entrada_cap

        ttk.Label(marco_contenido, text="Sistema de riego", style="TLabel").grid(row=2, column=2, sticky="w", pady=5, padx=10)
        combo_riego = ttk.Combobox(marco_contenido, values=["Manual", "Automatizado", "Por goteo"], width=28, style="TCombobox")
        combo_riego.grid(row=2, column=3, sticky="w", pady=5, padx=10)
        self.entradas['riego'] = combo_riego

        ttk.Label(marco_contenido, text="Visualización:", style="TLabel").grid(row=3, column=2, sticky="w", pady=(20,5), padx=10)
        visor_imagen = tk.Label(marco_contenido, bg=self.vista.light_bg, text="Vista Previa", width=30, height=10, relief="solid", borderwidth=1, fg="#AAAAAA") 
        visor_imagen.grid(row=4, column=2, columnspan=2, rowspan=3, pady=5, padx=10, sticky="nsew")

        marco_botones = ttk.Frame(marco_contenido, style="TFrame")
        marco_botones.grid(row=7, column=0, columnspan=4, pady=30)

        ttk.Button(
            marco_botones, 
            text="Guardar", 
            style="Green.TButton",
            command=self.al_guardar
        ).pack(side="left", padx=10)
        
        ttk.Button(
            marco_botones, 
            text="Cancelar", 
            style="Red.TButton",
            command=lambda: self.vista.mostrar_frame("FramePrincipal")
        ).pack(side="left", padx=10)

    def al_guardar(self):
        datos = {
            'nombre': self.entradas['nombre'].get(),
            'superficie': self.entradas['superficie'].get(),
            'tipo_cultivo': self.entradas['tipo'].get(),
            'fecha_creacion': self.entradas['fecha'].get(),
            'responsable': self.entradas['responsable'].get(),
            'capacidad_produccion': self.entradas['capacidad'].get(),
            'sistema_riego': self.entradas['riego'].get()
        }
        self.vista.controlador.manejar_guardar_invernadero(datos)


class FrameEnfermedad(ttk.Frame):
    def __init__(self, padre, vista):
        super().__init__(padre, style="TFrame")
        self.vista = vista
        
        marco_contenido = ttk.Frame(self, style="TFrame")
        marco_contenido.pack(fill="both", expand=True, padx=40, pady=20)
        
        ttk.Label(marco_contenido, text="Registrar Enfermedad", style="Header.TLabel").pack(pady=20, anchor="w")

        self.entradas = {}
        campos = ["Nombre común", "Nombre científico"]
        for campo in campos:
            f = ttk.Frame(marco_contenido, style="TFrame")
            f.pack(fill="x", pady=5)
            ttk.Label(f, text=campo, width=20, style="TLabel").pack(side="left")
            entrada = ttk.Entry(f, width=50, style="TEntry")
            entrada.pack(side="left", fill="x", expand=True, padx=10)
            self.entradas[campo.split(" ")[0].lower()] = entrada

        ttk.Label(marco_contenido, text="Síntomas", style="TLabel").pack(anchor="w", pady=(10,0))
        self.texto_sintomas = tk.Text(marco_contenido, height=5, width=60, relief="solid", borderwidth=1, font=("Segoe UI", 10), bd=1, highlightthickness=1, highlightcolor=self.vista.primary_color, highlightbackground="#BDBDBD")
        self.texto_sintomas.pack(fill="x", pady=5)
        
        ttk.Label(marco_contenido, text="Tratamiento", style="TLabel").pack(anchor="w", pady=(10,0))
        self.texto_tratamiento = tk.Text(marco_contenido, height=5, width=60, relief="solid", borderwidth=1, font=("Segoe UI", 10), bd=1, highlightthickness=1, highlightcolor=self.vista.primary_color, highlightbackground="#BDBDBD")
        self.texto_tratamiento.pack(fill="x", pady=5)
        
        marco_botones = ttk.Frame(marco_contenido, style="TFrame")
        marco_botones.pack(pady=20, anchor="center")
        
        ttk.Button(
            marco_botones, 
            text="Guardar", 
            style="Green.TButton",
            command=self.al_guardar
        ).pack(side="left", padx=10)
        
        ttk.Button(
            marco_botones, 
            text="Cancelar", 
            style="Red.TButton",
            command=lambda: self.vista.mostrar_frame("FramePrincipal")
        ).pack(side="left", padx=10)

    def al_guardar(self):
        dict_datos = {
            'nombre_comun': self.entradas['nombre'].get(),
            'nombre_cientifico': self.entradas['nombre'].get(),
            'sintomas': self.texto_sintomas.get("1.0", "end-1c"),
            'tratamiento': self.texto_tratamiento.get("1.0", "end-1c")
        }
        self.vista.controlador.manejar_guardar_enfermedad(dict_datos)


class FrameControlInvernadero(ttk.Frame):
    def __init__(self, padre, vista):
        super().__init__(padre, style="TFrame")
        self.vista = vista
        
        self.marco_cabecera = tk.Frame(self, bg=self.vista.light_bg, pady=10)
        self.marco_cabecera.pack(side="top", fill="x")
        ttk.Label(self.marco_cabecera, text="Control de Invernaderos", style="Header.TLabel", background=self.vista.light_bg).pack(padx=20, anchor="w")
        
        self.contenedor_lista = ttk.Frame(self, style="TFrame")
        self.contenedor_lista.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.marco_lista_invernaderos = ttk.Frame(self.contenedor_lista, style="TFrame")
        self.marco_lista_invernaderos.pack(fill="x", padx=10, pady=10)
        
        ttk.Button(
            self.contenedor_lista, 
            text="Regresar",
            style="Red.TButton",
            command=lambda: self.vista.mostrar_frame("FramePrincipal")
        ).pack(side="bottom", pady=10, anchor="e")

    def llenar_lista_invernaderos(self, invernaderos):
        for widget in self.marco_lista_invernaderos.winfo_children():
            widget.destroy()

        if not invernaderos:
            ttk.Label(self.marco_lista_invernaderos, text="No hay invernaderos registrados.", style="TLabel").pack(pady=20)
            return
            
        marco_cabecera_tabla = ttk.Frame(self.marco_lista_invernaderos, style="ListHeader.TFrame")
        marco_cabecera_tabla.pack(fill="x", pady=(0, 5))
        
        ttk.Label(marco_cabecera_tabla, text="Invernadero", width=25, anchor="w", style="ListHeader.TLabel").pack(side="left", padx=10, pady=5)
        ttk.Label(marco_cabecera_tabla, text="Operativo", width=10, anchor="center", style="ListHeader.TLabel").pack(side="left")
        ttk.Label(marco_cabecera_tabla, text="Reparación", width=10, anchor="center", style="ListHeader.TLabel").pack(side="left")
        ttk.Label(marco_cabecera_tabla, text="Inspección", width=10, anchor="center", style="ListHeader.TLabel").pack(side="left")
        ttk.Label(marco_cabecera_tabla, text="Expansión", width=10, anchor="center", style="ListHeader.TLabel").pack(side="left")
        ttk.Label(marco_cabecera_tabla, text="Acciones", width=30, anchor="e", style="ListHeader.TLabel").pack(side="right", padx=10)

        for inv in invernaderos:
            self._crear_fila_invernadero(inv)

    def _crear_fila_invernadero(self, datos_inv):
        marco_fila = ttk.Frame(self.marco_lista_invernaderos, style="ListRow.TFrame") 
        marco_fila.pack(fill="x", pady=2)
        
        id_inv = datos_inv.get('id', 'N/A')
        nombre_inv = datos_inv.get('nombre', 'Invernadero sin Nombre')
        estado_actual = datos_inv.get('estado', 'Operativo') 

        ttk.Label(marco_fila, text=nombre_inv, width=25, anchor="w", style="ListRow.TLabel").pack(side="left", padx=10, pady=5)

        var_estado = tk.StringVar(value=estado_actual)
        estados = ["Operativo", "Reparacion", "Inspeccion", "Expansión"]
        
        for estado in estados:
            rb = ttk.Radiobutton(
                marco_fila, 
                text="", 
                variable=var_estado, 
                value=estado, 
                width=10,
                style="TRadiobutton",
                command=lambda id=id_inv, est=estado: self.vista.controlador.manejar_cambio_estado(id, est)
            )
            rb.pack(side="left", padx=5)

        marco_acciones = ttk.Frame(marco_fila, style="ListRow.TFrame")
        marco_acciones.pack(side="right", padx=10)

        ttk.Button(
            marco_acciones, 
            text="Editar", 
            style="Edit.TButton",
            command=lambda id=id_inv: self.vista.controlador.manejar_accion_control(id, "editar")
        ).pack(side="left", padx=5)

        ttk.Button(
            marco_acciones, 
            text="Detalles", 
            style="Detail.TButton",
            command=lambda id=id_inv: self.vista.controlador.manejar_accion_control(id, "detalle")
        ).pack(side="left", padx=5)

        ttk.Button(
            marco_acciones, 
            text="Eliminar", 
            style="Delete.TButton",
            command=lambda id=id_inv: self.vista.controlador.manejar_accion_control(id, "eliminar")
        ).pack(side="left", padx=5)


class FrameEditarInvernadero(ttk.Frame):
    def __init__(self, padre, vista):
        super().__init__(padre, style="TFrame")
        self.vista = vista
        self.id_invernadero = None
        
        marco_contenido = ttk.Frame(self, style="TFrame")
        marco_contenido.pack(fill="both", expand=True, padx=40, pady=20)

        ttk.Label(marco_contenido, text="Editar Invernadero", style="Header.TLabel").grid(row=0, column=0, columnspan=4, pady=20, sticky="w")

        self.mapa_campos = {
            "nombre": "Nombre del invernadero",
            "superficie": "Superficie (m²)",
            "tipo_cultivo": "Tipo de cultivo",
            "fecha_creacion": "Fecha de creacion (YYYY-MM-DD)",
            "responsable": "Responsable del invernadero",
            "capacidad_produccion": "Capacidad de producción",
            "sistema_riego": "Sistema de riego"
        }
        
        self.entradas = {}
        
        campos_col1 = ["nombre", "superficie", "tipo_cultivo", "fecha_creacion", "responsable"]
        for i, clave_campo in enumerate(campos_col1):
            ttk.Label(marco_contenido, text=self.mapa_campos[clave_campo], style="TLabel").grid(row=i+1, column=0, sticky="w", pady=5, padx=10)
            entrada = ttk.Entry(marco_contenido, width=30, style="TEntry")
            entrada.grid(row=i+1, column=1, sticky="w", pady=5, padx=10)
            self.entradas[clave_campo] = entrada 

        ttk.Label(marco_contenido, text=self.mapa_campos["capacidad_produccion"], style="TLabel").grid(row=1, column=2, sticky="w", pady=5, padx=10)
        entrada_cap = ttk.Entry(marco_contenido, width=30, style="TEntry")
        entrada_cap.grid(row=1, column=3, sticky="w", pady=5, padx=10)
        self.entradas['capacidad_produccion'] = entrada_cap

        ttk.Label(marco_contenido, text=self.mapa_campos["sistema_riego"], style="TLabel").grid(row=2, column=2, sticky="w", pady=5, padx=10)
        combo_riego = ttk.Combobox(marco_contenido, values=["Manual", "Automatizado", "Por goteo"], width=28, style="TCombobox")
        combo_riego.grid(row=2, column=3, sticky="w", pady=5, padx=10)
        self.entradas['sistema_riego'] = combo_riego
        
        ttk.Label(marco_contenido, text="Estado (Solo se edita en Control)", style="TLabel").grid(row=3, column=2, sticky="w", pady=5, padx=10)
        self.etiqueta_estado = ttk.Label(marco_contenido, text="", style="TLabel", background=self.vista.light_bg, width=30, anchor="w", padding=5)
        self.etiqueta_estado.grid(row=3, column=3, sticky="w", pady=5, padx=10)

        ttk.Label(marco_contenido, text="Visualización:", style="TLabel").grid(row=4, column=2, sticky="w", pady=(20,5), padx=10)
        visor_imagen = tk.Label(marco_contenido, bg=self.vista.light_bg, text="Vista Previa", width=30, height=10, relief="solid", borderwidth=1, fg="#AAAAAA") 
        visor_imagen.grid(row=5, column=2, columnspan=2, rowspan=2, pady=5, padx=10, sticky="nsew")

        marco_botones = ttk.Frame(marco_contenido, style="TFrame")
        marco_botones.grid(row=7, column=0, columnspan=4, pady=30)

        ttk.Button(
            marco_botones, 
            text="Guardar Cambios", 
            style="Green.TButton",
            command=self.al_guardar_edicion
        ).pack(side="left", padx=10)
        
        ttk.Button(
            marco_botones, 
            text="Cancelar", 
            style="Red.TButton",
            command=lambda: self.vista.mostrar_frame("FrameControlInvernadero")
        ).pack(side="left", padx=10)

    def cargar_datos(self, datos):
        self.id_invernadero = datos.get('id')
        
        for clave, entrada in self.entradas.items():
            valor = datos.get(clave, '')
            if isinstance(entrada, ttk.Combobox):
                try:
                    indice = entrada['values'].index(valor)
                    entrada.current(indice)
                except ValueError:
                    entrada.set(valor) 
            else:
                entrada.delete(0, tk.END)
                entrada.insert(0, valor)
        
        self.etiqueta_estado.config(text=datos.get('estado', 'N/A'))


    def al_guardar_edicion(self):
        datos_a_actualizar = {
            'id': self.id_invernadero,
            'nombre': self.entradas['nombre'].get(),
            'superficie': self.entradas['superficie'].get(),
            'tipo_cultivo': self.entradas['tipo_cultivo'].get(),
            'fecha_creacion': self.entradas['fecha_creacion'].get(),
            'responsable': self.entradas['responsable'].get(),
            'capacidad_produccion': self.entradas['capacidad_produccion'].get(),
            'sistema_riego': self.entradas['sistema_riego'].get()
        }
        self.vista.controlador.manejar_guardar_edicion_invernadero(datos_a_actualizar)


class FrameHumedad(ttk.Frame):
    def __init__(self, padre, vista):
        super().__init__(padre, style="TFrame")
        self.vista = vista
        
        marco = ttk.Frame(self, style="TFrame")
        marco.place(relx=0.5, rely=0.5, anchor="center")
        
        ttk.Label(marco, text="Controlando la Humedad...", 
                  style="Blue.Header.TLabel").pack(pady=20)
                  
        ttk.Button(marco, 
                   text="Volver al Menú Principal", 
                   style="Red.TButton",
                   command=lambda: self.vista.mostrar_frame("FramePrincipal")
        ).pack(pady=10)


class FramePiso(ttk.Frame):
    def __init__(self, padre, vista):
        super().__init__(padre, style="TFrame")
        self.vista = vista
        
        marco = ttk.Frame(self, style="TFrame")
        marco.place(relx=0.5, rely=0.5, anchor="center")
        
        ttk.Label(marco, text="Ejecutando Control de Piso...", 
                  style="Orange.Header.TLabel").pack(pady=20)
                  
        ttk.Button(marco, 
                   text="Volver al Menú Principal", 
                   style="Red.TButton",
                   command=lambda: self.vista.mostrar_frame("FramePrincipal")
        ).pack(pady=10)


class Vista(tk.Tk):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador 
        
        self.main_bg = "#FFFFFF"
        self.light_bg = "#F5F5F5"
        self.primary_color = "#388E3C"
        self.accent_color = "#4CAF50"
        self.danger_color = "#D32F2F"
        self.warn_color = "#FFB300"
        self.info_color = "#78909C"

        self.title("Vivero Vital - GreenGrowth S.A.")
        self.geometry("1000x700") 
        self.configure(bg=self.main_bg)

        estilo = ttk.Style(self)
        estilo.theme_use('clam')

        estilo.configure("TFrame", background=self.main_bg)
        estilo.configure("TLabel", background=self.main_bg, font=("Segoe UI", 11))
        
        estilo.configure("Header.TLabel", 
                         font=("Segoe UI", 20, "bold"), 
                         foreground=self.primary_color, 
                         background=self.main_bg)
        
        estilo.configure("TEntry", 
                         font=("Segoe UI", 11), 
                         padding=5,
                         fieldbackground="#FDFDFD",
                         relief="solid",
                         borderwidth=1)
        estilo.map("TEntry", 
                   bordercolor=[('focus', self.primary_color), ('!focus', '#BDBDBD')],
                   relief=[('focus', 'solid'), ('!focus', 'solid')])
        
        estilo.configure("TCombobox", 
                         font=("Segoe UI", 11), 
                         padding=5,
                         fieldbackground="#FDFDFD",
                         arrowcolor=self.primary_color)
        estilo.map("TCombobox",
                   bordercolor=[('focus', self.primary_color), ('!focus', '#BDBDBD')],
                   relief=[('focus', 'solid'), ('!focus', 'solid')],
                   fieldbackground=[('readonly', self.main_bg)])
        
        estilo.configure("TRadiobutton", 
                         background=self.main_bg,
                         font=("Segoe UI", 10))
        estilo.map("TRadiobutton",
                   indicatorcolor=[('selected', self.primary_color), ('!selected', '#AAAAAA')],
                   background=[('active', self.light_bg)])

        estilo.configure("TButton", 
                         font=("Segoe UI", 11, "bold"), 
                         padding=(10, 8), 
                         borderwidth=0,
                         relief="flat",
                         background="#E0E0E0",
                         foreground="#333333")
        estilo.map("TButton",
                   background=[('active', '#BDBDBD')])

        estilo.configure("Green.TButton", 
                         background=self.accent_color, 
                         foreground="white")
        estilo.map("Green.TButton",
                   background=[('active', self.primary_color)])

        estilo.configure("Red.TButton", 
                         background=self.danger_color, 
                         foreground="white")
        estilo.map("Red.TButton",
                   background=[('active', '#B71C1C')])

        estilo.configure("Nav.TButton", 
                         font=("Segoe UI", 12, "bold"), 
                         padding=(15, 10),
                         background=self.accent_color,
                         foreground="white",
                         borderwidth=0,
                         relief="flat")
        estilo.map("Nav.TButton",
                   background=[('active', self.primary_color)])
        
        estilo.configure("NavRed.TButton", 
                         font=("Segoe UI", 12, "bold"), 
                         padding=(15, 10),
                         background=self.danger_color,
                         foreground="white",
                         borderwidth=0,
                         relief="flat")
        estilo.map("NavRed.TButton",
                   background=[('active', '#B71C1C')])

        estilo.configure("Detail.TButton", background=self.warn_color, foreground="black", font=("Segoe UI", 9, "bold"), padding=(5,5), borderwidth=0)
        estilo.map("Detail.TButton", background=[('active', '#FFA000')])
        
        estilo.configure("Edit.TButton", background=self.info_color, foreground="white", font=("Segoe UI", 9, "bold"), padding=(5,5), borderwidth=0)
        estilo.map("Edit.TButton", background=[('active', '#546E7A')])
        
        estilo.configure("Delete.TButton", background=self.danger_color, foreground="white", font=("Segoe UI", 9, "bold"), padding=(5,5), borderwidth=0)
        estilo.map("Delete.TButton", background=[('active', '#B71C1C')])

        estilo.configure("ListHeader.TFrame", background=self.light_bg)
        estilo.configure("ListHeader.TLabel", 
                         font=("Segoe UI", 10, "bold"), 
                         background=self.light_bg, 
                         foreground=self.primary_color,
                         padding=(0, 5))
                         
        estilo.configure("ListRow.TFrame", background=self.main_bg, borderwidth=1, relief="solid", bordercolor="#EEEEEE")
        estilo.configure("ListRow.TLabel", background=self.main_bg, font=("Segoe UI", 10))
        estilo.configure("ListRow.TFrame", background=self.main_bg)
        
        estilo.configure("Blue.Header.TLabel", background=self.main_bg, font=("Segoe UI", 18, "bold"), foreground="#0277BD")
        estilo.configure("Orange.Header.TLabel", background=self.main_bg, font=("Segoe UI", 18, "bold"), foreground="#FF6F00")

        self.contenedor = tk.Frame(self, bg=self.main_bg)
        self.contenedor.pack(side="top", fill="both", expand=True)
        self.contenedor.grid_rowconfigure(0, weight=1)
        self.contenedor.grid_columnconfigure(0, weight=1)

        self.marcos = {}
        
        self.crear_marcos() 
        self.mostrar_frame("FrameLogin")

    def crear_marcos(self):
        for ClaseFrame in (FrameLogin, FramePrincipal, FrameRegistroInvernadero, FrameEnfermedad, FrameControlInvernadero, FrameHumedad, FramePiso, FrameEditarInvernadero):
            nombre_frame = ClaseFrame.__name__
            marco = ClaseFrame(padre=self.contenedor, vista=self) 
            self.marcos[nombre_frame] = marco
            marco.grid(row=0, column=0, sticky="nsew")

    def mostrar_frame(self, nombre_frame):
        marco = self.marcos[nombre_frame]
        
        if nombre_frame == "FrameControlInvernadero":
            if self.controlador: 
                self.controlador.manejar_cargar_control_invernaderos()
            
        marco.tkraise()
        
    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje)
        elif tipo == "warning":
            messagebox.showwarning(titulo, mensaje)
        else:
            messagebox.showinfo(titulo, mensaje)

    def actualizar_frame_control(self, datos):
        if "FrameControlInvernadero" in self.marcos:
            self.marcos["FrameControlInvernadero"].llenar_lista_invernaderos(datos)