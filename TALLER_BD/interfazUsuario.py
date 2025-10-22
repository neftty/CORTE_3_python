import tkinter as Ventana
from Productos import Productos  
from Clientes import Clientes   


class InterfazTienda:
    def __init__(self):
        self.producto = Productos()
        self.cliente = Clientes()
        self.formulario = " "

        self.entryIdP = " "
        self.entryNombreP = " "
        self.entryPrecioP = " "
        self.entryStockP = " "
        self.entryCategoriaP = " "

        self.entryIdC = " "
        self.entryNombreC = " "
        self.entryApellidoC = " "
        self.entryEmailC = " "
        self.entryHistorialC = " "

    def getIdP(self): 
        return self.entryIdP.get()
    
    def getNombreP(self): 
        return self.entryNombreP.get()
    
    def getPrecioP(self): 
        return self.entryPrecioP.get()
    
    def getStockP(self): 
        return self.entryStockP.get()
    
    def getCategoriaP(self): return self.entryCategoriaP.get()

    def setIdP(self, valor):
        self.entryIdP.delete(0, 'end')
        self.entryIdP.insert(0, valor)

    def setNombreP(self, valor):
        self.entryNombreP.delete(0, 'end')
        self.entryNombreP.insert(0, valor)

    def setPrecioP(self, valor):
        self.entryPrecioP.delete(0, 'end')
        self.entryPrecioP.insert(0, valor)

    def setStockP(self, valor):
        self.entryStockP.delete(0, 'end')
        self.entryStockP.insert(0, valor)

    def setCategoriaP(self, valor):
        self.entryCategoriaP.delete(0, 'end')
        self.entryCategoriaP.insert(0, valor)


    def getIdC(self): 
        return self.entryIdC.get()
    
    def getNombreC(self): 
        return self.entryNombreC.get()
    
    def getApellidoC(self): 
        return self.entryApellidoC.get()
    
    def getEmailC(self): 
        return self.entryEmailC.get()
    
    def getHistorialC(self): 
        return self.entryHistorialC.get()

    def setIdC(self, valor):
        self.entryIdC.delete(0, 'end')
        self.entryIdC.insert(0, valor)

    def setNombreC(self, valor):
        self.entryNombreC.delete(0, 'end')
        self.entryNombreC.insert(0, valor)

    def setApellidoC(self, valor):
        self.entryApellidoC.delete(0, 'end')
        self.entryApellidoC.insert(0, valor)

    def setEmailC(self, valor):
        self.entryEmailC.delete(0, 'end')
        self.entryEmailC.insert(0, valor)

    def setHistorialC(self, valor):
        self.entryHistorialC.delete(0, 'end')
        self.entryHistorialC.insert(0, valor)


    def iniciarVentana(self):
        self.formulario = Ventana.Tk()
        self.formulario.title("Gestión Tienda CRUD")
        self.formulario.geometry("900x700")
        self.formulario.configure(bg="lightblue")

        Ventana.Label(self.formulario, text="SISTEMA DE TIENDA", font=("Arial", 20, "bold"), 
                      bg="lightblue", fg="red").pack(pady=15)
        Ventana.Button(self.formulario, text="Módulo Productos", bg="#3498DB", fg="white", 
                       width=25, font=("Arial", 12, "bold"), 
                       command=lambda: self.moduloProductos()).pack(pady=5)
        Ventana.Button(self.formulario, text="Módulo Clientes", bg="#2ECC71", fg="white", 
                       width=25, font=("Arial", 12, "bold"), 
                       command=lambda: self.moduloClientes()).pack(pady=5)
        
        return self.formulario

    def moduloProductos(self):
        ventana = Ventana.Toplevel()
        ventana.title("Módulo Productos")
        ventana.geometry("750x650")
        ventana.configure(bg="#3498DB")  

        Ventana.Label(ventana, text="GESTIÓN DE PRODUCTOS", font=("Arial", 18, "bold"), bg="#3498DB", fg="white").pack(pady=10)

        Ventana.Label(ventana, text="ID:", bg="#3498DB", fg="white").pack()
        self.entryIdP = Ventana.Entry(ventana, width=20)
        self.entryIdP.pack()

        Ventana.Label(ventana, text="Nombre:", bg="#3498DB", fg="white").pack()
        self.entryNombreP = Ventana.Entry(ventana, width=40)
        self.entryNombreP.pack()

        Ventana.Label(ventana, text="Precio:", bg="#3498DB", fg="white").pack()
        self.entryPrecioP = Ventana.Entry(ventana, width=40)
        self.entryPrecioP.pack()

        Ventana.Label(ventana, text="Stock:",bg="#3498DB", fg="white").pack()
        self.entryStockP = Ventana.Entry(ventana, width=40)
        self.entryStockP.pack()

        Ventana.Label(ventana, text="Categoría:",bg="#3498DB", fg="white").pack()
        self.entryCategoriaP = Ventana.Entry(ventana, width=40)
        self.entryCategoriaP.pack()

        resultado = Ventana.Label(ventana, text="", bg="#3498DB", fg="black", font=("Arial", 11), justify="left")
        resultado.pack(pady=10)

        Ventana.Button(ventana, text="Agregar", bg="green", fg="white", width=15, command=lambda: self.agregarProducto(self.entryIdP, self.entryNombreP, self.entryPrecioP, self.entryStockP, self.entryCategoriaP, resultado)).pack(pady=3)
        
        Ventana.Button(ventana, text="Consultar", bg="blue", fg="white", width=15, command=lambda: self.consultarProductos(resultado)).pack(pady=3)
        Ventana.Button(ventana, text="Actualizar", bg="orange", fg="black", width=15, command=lambda: self.actualizarProducto(self.entryIdP, self.entryNombreP, self.entryPrecioP, self.entryStockP, self.entryCategoriaP, resultado)).pack(pady=3)
        Ventana.Button(ventana, text="Eliminar", bg="red", fg="white", width=15, command=lambda: self.eliminarProducto(self.entryIdP, resultado)).pack(pady=3)

        Ventana.Button(ventana, text="Valor total inventario", bg="purple", fg="white", width=25, command=lambda: self.valorInventario(resultado)).pack(pady=3)
        Ventana.Button(ventana, text="Valor por categoría", bg="yellow", fg="black", width=25, command=lambda: self.valorPorCategoria(resultado)).pack(pady=3)
        Ventana.Button(ventana, text="Productos con stock bajo (<5)", bg="brown", fg="white", width=30, command=lambda: self.productosStockBajo(resultado)).pack(pady=3)

    def agregarProducto(self, idp, nombre, precio, stock, categoria, label):
        try:
            try:
                id_int = int(idp.get())
                precio_float = float(precio.get())
                stock_int = int(stock.get())
            except ValueError:
                label.config(text="Error: 'ID', 'Precio' y 'Stock' deben ser números.")
                return 
            
            self.producto.agregarProducto(id_int, nombre.get(), precio_float, stock_int, categoria.get())
            label.config(text="Producto agregado correctamente")
            self.consultarProductos(label) 
        except Exception as e:
            label.config(text=f"Error al agregar producto: {e}")
        finally:
            self.setIdP("")
            self.setNombreP("")
            self.setPrecioP("")
            self.setStockP("")
            self.setCategoriaP("")

    def consultarProductos(self, label):
        try:
            datos = self.producto.consultarProductos()
            texto = "ID | Nombre | Precio | Stock | Categoría\n"
            texto += "----------------------------------------------\n"
            texto += "\n".join(f"{fila[0]} | {fila[1]} | {fila[2]} | {fila[3]} | {fila[4]}" for fila in datos)
            label.config(text=texto)
        except Exception as e:
            label.config(text=f"Error al consultar productos: {e}")

    def actualizarProducto(self, idp, nombre, precio, stock, categoria, label):
        try:
            try:
                id_int = int(idp.get())
                precio_float = float(precio.get())
                stock_int = int(stock.get())
            except ValueError:
                label.config(text="Error: 'ID', 'Precio' y 'Stock' deben ser números.")
                return

            self.producto.actualizarProducto(id_int, nombre.get(), precio_float, stock_int, categoria.get())
            label.config(text=f"Producto {idp.get()} actualizado")
            self.consultarProductos(label) 
        except Exception as e:
            label.config(text=f"Error al actualizar producto: {e}")
        finally:
            self.setIdP("")
            self.setNombreP("")
            self.setPrecioP("")
            self.setStockP("")
            self.setCategoriaP("")

    def eliminarProducto(self, idp, label):
        try:
            try:
                id_int = int(idp.get())
            except ValueError:
                label.config(text="Error: El 'ID' debe ser un número.")
                return
            
            self.producto.eliminarProducto(id_int)
            label.config(text=f"Producto {idp.get()} eliminado")
            self.consultarProductos(label) 
        except Exception as e:
            label.config(text=f"Error al eliminar producto: {e}")
        finally:
            self.setIdP("")

    def valorInventario(self, label):
        try:
            total = self.producto.valorTotalInventario()
            label.config(text=f"Valor total del inventario: ${total:,.2f}")
        except Exception as e:
            label.config(text=f"Error al calcular inventario: {e}")

    def valorPorCategoria(self, label):
        try:
            datos = self.producto.valorPorCategoria()
            texto = "Valor por Categoría:\n"
            texto += "-----------------------\n"
            texto += "\n".join(f"Categoría: {d[0]} - Valor: ${d[1]:,.2f}" for d in datos)
            label.config(text=texto)
        except Exception as e:
            label.config(text=f"Error al calcular valor por categoría: {e}")

    def productosStockBajo(self, label):
        try:
            datos = self.producto.productosStockBajo(5) 
            if not datos:
                label.config(text="No hay productos con stock bajo (<5)")
            else:
                texto = "Productos con Stock Bajo (<5):\n"
                texto += "ID | Nombre | Stock\n"
                texto += "-----------------------\n"
                texto += "\n".join(f"{fila[0]} | {fila[1]} | {fila[3]}" for fila in datos) 
                label.config(text=texto)
        except Exception as e:
            label.config(text=f"Error al consultar stock bajo: {e}")


    def moduloClientes(self):
        ventana = Ventana.Toplevel()
        ventana.title("Módulo Clientes")
        ventana.geometry("750x650")
        ventana.configure(bg="#3a8f3a")  

        Ventana.Label(ventana, text="GESTIÓN DE CLIENTES", font=("Arial", 18, "bold"), bg="#3a8f3a", fg="white").pack(pady=10)

        Ventana.Label(ventana, text="ID:", bg="#3a8f3a", fg="white").pack()
        self.entryIdC = Ventana.Entry(ventana, width=20)
        self.entryIdC.pack()
        
        Ventana.Label(ventana, text="Nombre:", bg="#3a8f3a", fg="white").pack()
        self.entryNombreC = Ventana.Entry(ventana, width=40)
        self.entryNombreC.pack()

        Ventana.Label(ventana, text="Apellido:", bg="#3a8f3a", fg="white").pack()
        self.entryApellidoC = Ventana.Entry(ventana, width=40)
        self.entryApellidoC.pack()

        Ventana.Label(ventana, text="Email:", bg="#3a8f3a", fg="white").pack()
        self.entryEmailC = Ventana.Entry(ventana, width=40)
        self.entryEmailC.pack()

        Ventana.Label(ventana, text="Historial de compras:", bg="#3a8f3a", fg="white").pack()
        self.entryHistorialC = Ventana.Entry(ventana, width=40)
        self.entryHistorialC.pack()

        resultado = Ventana.Label(ventana, text="", bg="#3a8f3a", fg="black", font=("Arial", 11), justify="left")
        resultado.pack(pady=10)

        Ventana.Button(ventana, text="Agregar", bg="blue", fg="white", width=15, command=lambda: self.agregarCliente(self.entryIdC, self.entryNombreC, self.entryApellidoC, self.entryEmailC, self.entryHistorialC, resultado)).pack(pady=3)
        
        Ventana.Button(ventana, text="Consultar", bg="purple", fg="white", width=15, command=lambda: self.consultarClientes(resultado)).pack(pady=3)
        Ventana.Button(ventana, text="Actualizar", bg="orange", fg="black", width=15, command=lambda: self.actualizarCliente(self.entryIdC, self.entryNombreC, self.entryApellidoC, self.entryEmailC, self.entryHistorialC, resultado)).pack(pady=3)
        Ventana.Button(ventana, text="Eliminar", bg="red", fg="white", width=15, command=lambda: self.eliminarCliente(self.entryIdC, resultado)).pack(pady=3)

        Ventana.Button(ventana, text="Valor total de compras", bg="brown", fg="white", width=25, command=lambda: self.totalCompras(resultado)).pack(pady=3)
        Ventana.Button(ventana, text="Total por cliente", bg="yellow", fg="black", width=25, command=lambda: self.totalPorCliente(resultado)).pack(pady=3)

    def agregarCliente(self, idc, nombre, apellido, email, historial, label):
        try:
            try:
                id_int = int(idc.get())
                historial_float = float(historial.get())
            except ValueError:
                label.config(text="Error: 'ID' e 'Historial' deben ser números.")
                return
            
            self.cliente.agregarCliente(id_int, nombre.get(), apellido.get(), email.get(), historial_float)
            label.config(text="Cliente agregado correctamente")
            self.consultarClientes(label) 
        except Exception as e:
            label.config(text=f"Error al agregar cliente: {e}")
        finally:
            self.setIdC("")
            self.setNombreC("")
            self.setApellidoC("")
            self.setEmailC("")
            self.setHistorialC("")

    def consultarClientes(self, label):
        try:
            datos = self.cliente.consultarClientes()
            texto = "ID | Nombre | Apellido | Email | Historial\n"
            texto += "---------------------------------------------------\n"
            texto += "\n".join(f"{fila[0]} | {fila[1]} | {fila[2]} | {fila[3]} | ${fila[4]:,.2f}" for fila in datos)
            label.config(text=texto)
        except Exception as e:
            label.config(text=f"Error al consultar clientes: {e}")

    def actualizarCliente(self, idc, nombre, apellido, email, historial, label):
        try:
            try:
                id_int = int(idc.get())
                historial_float = float(historial.get())
            except ValueError:
                label.config(text="Error: 'ID' e 'Historial' deben ser números.")
                return
            
            self.cliente.actualizarCliente(id_int, nombre.get(), apellido.get(), email.get(), historial_float)
            label.config(text=f"Cliente {idc.get()} actualizado")
            self.consultarClientes(label) 
        except Exception as e:
            label.config(text=f"Error al actualizar cliente: {e}")
        finally:
            self.setIdC("")
            self.setNombreC("")
            self.setApellidoC("")
            self.setEmailC("")
            self.setHistorialC("")

    def eliminarCliente(self, idc, label):
        try:
            try:
                id_int = int(idc.get())
            except ValueError:
                label.config(text="Error: El 'ID' debe ser un número.")
                return
            
            self.cliente.eliminarCliente(id_int)
            label.config(text=f"Cliente {idc.get()} eliminado")
            self.consultarClientes(label) 
        except Exception as e:
            label.config(text=f"Error al eliminar cliente: {e}")
        finally:
            self.setIdC("")

    def totalCompras(self, label):
        try:
            total = self.cliente.valorTotalCompras()
            label.config(text=f"Valor total de compras: ${total:,.2f}")
        except Exception as e:
            label.config(text=f"Error al calcular total: {e}")

    def totalPorCliente(self, label):
        try:
            datos = self.cliente.totalComprasPorCliente()
            texto = "Total de Compras por Cliente:\n"
            texto += "----------------------------------\n"
            texto += "\n".join(f"{d[0]} {d[1]} → ${d[2]:,.2f}" for d in datos)
            label.config(text=texto)
        except Exception as e:
            label.config(text=f"Error al calcular total por cliente: {e}")


if __name__ == "__main__": 
    obj = InterfazTienda()
    aux = obj.iniciarVentana()
    aux.mainloop()