class Nodo:
    def __init__(self, documento, nombre):
        self.documento =documento
        self.nombre = nombre 
        self.siguiente= None
class lista:
    def __init__(self):
        self.cabeza=None
#agregar otro nodo al final de ultimo 
    def agregarAlFinal(self,documento, nombre ):
        nodo = Nodo(documento, nombre)

        if self.cabeza== None:
            self.cabeza=nodo
        else:
            actual =self.cabeza
            while actual.siguiente:
                actual=actual.siguiente
            actual.siguiente= nodo

    
            
# comportamiento linel 

# apuntador del la cabeza a la cola para mejorar el codigo 




        
class Nodo:
    def __init__(self, documento, nombre):
        self.documento =documento
        self.nombre = nombre 
        self.siguiente= None
class lista:
    def __init__(self):
        self.cabeza=None
        self.cola= None
#agregar otro nodo al final de ultimo 
    def agregarAlFinal(self,documento, nombre ):
        nodo = Nodo(documento, nombre)

        if self.cabeza== None:
            self.cabeza=nodo
            self.cola=nodo
        else:
            self.cola.siguiente=nodo
            self.cola=nodo

        