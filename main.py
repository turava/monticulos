from Paciente import Paciente
from SalaEmergencias import SalaEmergencias

# Crear una instancia de SalaEmergencias
sala_emergencias = SalaEmergencias()

# Agregar pacientes a la sala de emergencias
paciente1 = Paciente(nombre="Paciente1", nivel_urgencia=8, horas_espera=3)
paciente2 = Paciente(nombre="Paciente2", nivel_urgencia=10, horas_espera=6)
paciente3 = Paciente(nombre="Paciente3", nivel_urgencia=7, horas_espera=2)

sala_emergencias.agregar_paciente(paciente1)
sala_emergencias.agregar_paciente(paciente2)
sala_emergencias.agregar_paciente(paciente3)

# Atender pacientes
for _ in range(20):
    paciente_atendido = sala_emergencias.atender_pacientes()
    sala_emergencias.atender_pacientes()
    if paciente_atendido:
        print(f"Paciente atendido: {paciente_atendido}")
    else:
        print("No hay pacientes para atender en este momento.")


# Después de la simulación
print("Informe de atención a pacientes:")
for i, (paciente, tiempo_espera) in enumerate(sala_emergencias.pacientes_atendidos, 1):
    if isinstance(paciente, Paciente):
        print(f"{i}. Paciente: {paciente.nombre}, Nivel de urgencia: {paciente.nivel_urgencia}, "
              f"Horas de espera: {tiempo_espera} horas")
    else:
        print(f"{i}. Paciente desconocido, Tiempo de espera: {tiempo_espera} horas")
