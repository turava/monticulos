from Monticulos.MonticulosSinHerencia.MaxHeap import MaxHeap
from Monticulos.MonticulosSinHerencia.MinHeap import MinHeap
from Paciente import Paciente

class SalaEmergencias:
    def __init__(self):
        self.max_heap = MaxHeap()
        self.min_heap = MinHeap()
        self.pacientes_atendidos = []

    def agregar_paciente(self, paciente):
        self.max_heap.push(paciente.nivel_urgencia)
        self.min_heap.push(paciente.horas_espera)

    def atender_pacientes(self):
        for _ in range(20):  # Simulación de atención a 20 pacientes
            if not self.max_heap.is_empty():
                paciente_urgente = self.max_heap.pop()
                tiempo_espera = self.calcular_tiempo_espera(paciente_urgente)
                print(f"Atendiendo paciente urgente: {paciente_urgente}, Tiempo de espera: {tiempo_espera} horas")
                self.pacientes_atendidos.append((paciente_urgente, tiempo_espera))

            elif not self.min_heap.is_empty() and self.min_heap.peek().value > 5:
                paciente_tiempo_espera = self.min_heap.pop()
                tiempo_espera = self.calcular_tiempo_espera(paciente_tiempo_espera)
                print(f"Atendiendo paciente por tiempo de espera: {paciente_tiempo_espera}, Tiempo de espera: {tiempo_espera} horas")
                self.pacientes_atendidos.append((paciente_tiempo_espera, tiempo_espera))

            elif not self.min_heap.is_empty():
                paciente_general = self.min_heap.pop()
                tiempo_espera = self.calcular_tiempo_espera(paciente_general)
                print(f"Atendiendo paciente general: {paciente_general}, Tiempo de espera: {tiempo_espera} horas")
                self.pacientes_atendidos.append((paciente_general, tiempo_espera))
        return self.pacientes_atendidos
           # else:
               # print("No hay más pacientes para atender.")
    
    def calcular_tiempo_espera(self, paciente):
        if isinstance(paciente, Paciente):
            tiempo_espera_calculado = paciente.horas_espera
            if hasattr(paciente, 'tiempo_espera_acumulado'):
                tiempo_espera_calculado += paciente.tiempo_espera_acumulado
            paciente.tiempo_espera_acumulado = tiempo_espera_calculado
            return tiempo_espera_calculado
        else:
            return 0

    # Otros métodos según sea necesario