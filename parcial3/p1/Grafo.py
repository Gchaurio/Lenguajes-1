# Grafo DIRIGIDO
class Grafo:
    def __init__(self):
        self.nodos = set()
        self.adyacentes = {}

    def agregar_nodo(self, nodo):
        self.nodos.add(nodo)
        self.adyacentes[nodo] = set()

    def agregar_arco(self, nodo_origen, nodo_destino):
        self.adyacentes[nodo_origen].add(nodo_destino)

    def obtener_adyacentes(self, nodo):
        return self.adyacentes[nodo]

    def imprimir_grafo(self):
        for nodo in self.nodos:
            if len(self.obtener_adyacentes(nodo)) == 0:
                print(nodo, "-> Sin Nodos Adyacentes" )
            else:
                print(nodo, "->", self.obtener_adyacentes(nodo))
