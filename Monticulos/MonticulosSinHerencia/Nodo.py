class Nodo:
    '''
    Clase Nodo para representar un nodo en estructuras de datos basadas en árboles.

    Atributos:
    valor (Any): El valor almacenado en el nodo.
    hijo_izquierda (Nodo): Referencia al hijo izquierdo del nodo.
    hijo_derecha (Nodo): Referencia al hijo derecho del nodo.
    '''

    def __init__(self, value):
        '''
        Inicializa un nuevo nodo.

        :param valor: El valor a almacenar en el nodo.
        '''
        self.value = value
        self.next = None


    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        '''
        Representación en cadena del empleado, mostrando su número identificador.

        :return: Representación en cadena del número identificador del empleado.
        '''
        return str(self.value) if hasattr(self.value, '__str__') else repr(self.value)