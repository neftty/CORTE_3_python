class modelo_numero:
    def __init__(self):
        self.dato_numero = " "
        
    def get_numero(self):
        return self.dato_numero
    
    def set_numero(self, nuevo_numero):
        self.dato_numero = nuevo_numero

    def validar_par_impar(self):
        if self.dato_numero % 2 == 0:
            mensaje= "El número es PAR"
        else:
            mensaje= "El número es IMPAR"
            
        return mensaje

    def validar_signo(self):
        if self.dato_numero == 0:
            mensaje = "El número es NEUTRO (CERO)"
        elif self.dato_numero > 0:
            mensaje = "El número es POSITIVO"
        else:
            mensaje = "El número es NEGATIVO"
        
        return mensaje


