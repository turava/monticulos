class Paciente:
    def __init__(self, nombre, nivel_urgencia, horas_espera):
        self.nombre = nombre
        self.nivel_urgencia = nivel_urgencia
        self.horas_espera = horas_espera

    def __lt__(self, other):
        return self.nivel_urgencia < other.nivel_urgencia

    def __str__(self):
        return f"{self.nombre} - Nivel de urgencia: {self.nivel_urgencia}, Horas de espera: {self.horas_espera}"
    
    def calcular_tiempo_espera(self):
            return self.horas_espera
