# Monticulos 
## Sistema de Prioridades en una Sala de Emergencias con Montículos Máx y Mín


# Sala de Emergencias - Gestión de Pacientes

Este proyecto simula la gestión de pacientes en una sala de emergencias utilizando dos montículos: uno máximo para la urgencia de atención médica y uno mínimo para el tiempo de espera de los pacientes. La implementación incluye las clases `Paciente` y `SalaEmergencias`.

## Clase Paciente

La clase `Paciente` tiene los siguientes atributos:

- `nombre`: El nombre del paciente.
- `nivel_urgencia`: Representa la urgencia de atención médica, siendo 10 el nivel más alto.
- `horas_espera`: El tiempo que el paciente ha esperado, en horas.

## Clase SalaEmergencias

La clase `SalaEmergencias` gestiona la atención de los pacientes. Incluye montículos máximos y mínimos como atributos para representar la urgencia y el tiempo de espera, respectivamente.

### Métodos:

- `agregar_paciente(paciente)`: Agrega un paciente a ambos montículos.
- `atender_pacientes()`: Desencola y atiende a los pacientes siguiendo las reglas establecidas.
- `calcular_tiempo_espera(paciente)`: Calcula el tiempo de espera de un paciente según las reglas especificadas.

## Simulación

Se genera una lista de pacientes aleatorios con niveles de urgencia y tiempos de espera variados. Los tiempos de espera se encuentran en una horquilla de entre 0h (acaba de llegar) y 12h (máximo). Los pacientes se incorporan a la `SalaEmergencias` asegurando su inclusión en ambos montículos.

## Atención

Se atienden a los pacientes según las reglas establecidas:
- Si hay pacientes con un nivel de urgencia de 10, se atienden inmediatamente.
- Si no hay pacientes con urgencia máxima pero hay pacientes que han esperado más de 5 horas, se atienden.
- En caso contrario, se atiende al paciente con la mayor urgencia.

## Reporte

Después de simular la atención de 20 pacientes, se genera un reporte que muestra los pacientes atendidos, en qué orden y después de cuánto tiempo de espera.
