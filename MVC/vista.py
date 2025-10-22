class vista:
    def __init__(self):
        self.nombre_modulo = "Validar Numeros"
        self.pregunta_numero = "Escribe un numero: "
        self.campo_numero = ""

    def hacer_campo(self):
        print(self.nombre_modulo)
        print(self.pregunta_numero)
        self.campo_numero = int(input())
        return self.campo_numero
    
    def imprimir_resultado(self, dato_mensaje):
        print(dato_mensaje)



