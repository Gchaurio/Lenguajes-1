class Secuencia:
    def __init__(self):
        self.elementos = []

    def agregar(self, elemento):
        raise NotImplementedError()

    def remover(self):
        raise NotImplementedError()

    def esta_vacia(self):
        raise NotImplementedError()

class Pila(Secuencia):
    def __init__(self):
        super().__init__()

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def remover(self):
        return self.elementos.pop(-1)
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
class Cola(Secuencia):
    def __init__(self):
        super().__init__()

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def remover(self):
        return self.elementos.pop(0)
    
    def esta_vacia(self):
        return len(self.elementos) == 0