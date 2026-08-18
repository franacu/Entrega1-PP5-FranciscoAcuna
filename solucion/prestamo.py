class Prestamo:
    def __init__(self, titulo, nombre_socio, dias_transcurridos):
        if titulo == "" or nombre_socio == "" or dias_transcurridos < 0:
            raise ValueError

        self.titulo = titulo
        self.nombre_socio = nombre_socio
        self.dias_transcurridos = dias_transcurridos
        
    def esta_vencido(self):
        if self.dias_transcurridos > 7:
            return True
        else:
            return False

    def dias_de_retraso(self):
        if self.dias_transcurridos > 7:
            return self.dias_transcurridos - 7
        else:
            return 0

#print(f"El nombre es {self.nombre_socio}, tenés {self.dias_de_retraso()} dias de retraso")
#si no usas el f --> te muestra exactamente lo que escribiste
#La f sirve para meter variables o resultados dentro de un texto de forma fácil.
# En un return no se coloca print porque primero se imprime la info, y despues el return actua. Si pones print, devuelve None.

    def resumen(self):
        if self.esta_vencido():
            return f"{self.titulo} — {self.nombre_socio} — vencido ({self.dias_de_retraso()} días)" 
            #   "El senor de los anillos — Frodo — vencido (1 días)" 
        else:
            return f"{self.titulo} — {self.nombre_socio} — en término"
            # "El senor de los anillos — Frodo — en término"
        