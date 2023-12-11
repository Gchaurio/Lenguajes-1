from Secuencia import *
from Grafo import *

class Busqueda:
    def __init__(self, g: Grafo):
        self.visitados = set()
        self.g = g

    def buscar(self, D, H):
        raise NotImplementedError()


class DFS(Busqueda):
    def buscar(self, D, H):
        self.visitados.clear()
        stack = Pila()
        stack.agregar(D)

        while not stack.esta_vacia():
            nodo_actual = stack.remover()
            self.visitados.add(nodo_actual)

            if nodo_actual == H:
                return len(self.visitados)
            
            for nodo in self.g.obtener_adyacentes(nodo_actual):
                if nodo not in self.visitados:
                    stack.agregar(nodo)


        return -1


class BFS(Busqueda):
    def buscar(self, D, H):
        self.visitados.clear()
        queue = Cola()
        queue.agregar(D)

        while not queue.esta_vacia():
            nodo_actual = queue.remover()
            self.visitados.add(nodo_actual)

            if nodo_actual == H:
                return len(self.visitados)

            for nodo in self.g.obtener_adyacentes(nodo_actual):
                if nodo not in self.visitados:
                    queue.agregar(nodo)

        return -1