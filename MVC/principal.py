from controlador import controlador
from modelo_numero import modelo_numero
from vista import vista

obj_modelo = modelo_numero()
obj_vista = vista()
obj_controlador = controlador(obj_vista, obj_modelo)


obj_controlador.hacer_pregunta()
