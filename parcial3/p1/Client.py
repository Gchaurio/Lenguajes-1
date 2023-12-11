from Busqueda import *
from Grafo import *

grafo = Grafo()

grafo.agregar_nodo(1)
grafo.agregar_nodo(2)
grafo.agregar_nodo(3)
grafo.agregar_nodo(4)
grafo.agregar_nodo(5)
grafo.agregar_nodo(6)
grafo.agregar_nodo(7)

grafo.agregar_arco(1, 2)
grafo.agregar_arco(1, 3)
grafo.agregar_arco(1, 6)
grafo.agregar_arco(2, 5)
grafo.agregar_arco(6, 5)
grafo.agregar_arco(3, 7)

print("Grafo:")
grafo.imprimir_grafo()

busqueda = DFS(grafo)

print("\nDFS")
print("Numero de nodos explorados (Nodos sobre los cuales nos paramos incluyendo el nodo inicial y objetivo) desde el nodo 1 al 5:")
print(busqueda.buscar(1, 5))
print("Numero de nodos explorados (Nodos sobre los cuales nos paramos incluyendo el nodo inicial y objetivo) desde el nodo 1 al 7:")
print(busqueda.buscar(1, 7))

busqueda = BFS(grafo)

print("\nBFS")
print("Numero de nodos explorados (Nodos sobre los cuales nos paramos incluyendo el nodo inicial y objetivo) desde el nodo 1 al 5:")
print(busqueda.buscar(1, 5))
print("Numero de nodos explorados (Nodos sobre los cuales nos paramos incluyendo el nodo inicial y objetivo) desde el nodo 1 al 7:")
print(busqueda.buscar(1, 7))