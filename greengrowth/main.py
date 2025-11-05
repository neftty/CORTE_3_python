import modelo
import vista
import controlador

if __name__ == "__main__":
    modelo_instancia = modelo.Modelo()
    vista_instancia = vista.Vista(None) 
    controlador_instancia = controlador.Controlador(modelo_instancia, vista_instancia) 
    vista_instancia.controlador = controlador_instancia
    vista_instancia.mainloop()