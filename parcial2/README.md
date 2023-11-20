# Lenguajes-1/ Parical 2
## Para correr los scripts de c, basta con correr los makes.

En cada Carpeta, se encuentra el algoritmo deseado junto con pruebas.
Para Chruch, se realiza una simple declaracion de church ademas de operacion entre datos del tipo church y sus resultados. 
Para arbol, se crean dos arboles, uno donde se cumple simetria y maxheap y otro donde no se cumple la simetria, pero sigue siendo un max heap. La funcion evalua correctamente ambos arboles.

## Las preguntas 2, 3 y 5 cuentan con clientes ejecutables.

El cliente del manejador de expresiones, puede correrse llamando a client.py.
El cliente de la lista de  enteros con elementos unicos sin repeticiones, se corre llamando al archivo unique_iter.py junto con la lista
  Ej:
    py unique_iter.py 1 4 3 2 5
  Este devolera las listas en orden.
El cliente del manejador de tripo de datos, corre al llamar a client.py

## La pregunta 4, contiene graficas, datos recolectados de las corridas y una conclusion acerca de el funcionamiento y eficiencia de los algoritmos dentro del archivo analysis.ipynb

## Para correr las pruebas unitarias de las preguntas 2, 4 y 5:

coverage run -m pytest
coverage report
