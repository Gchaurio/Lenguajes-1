# Lenguajes-1/ Parcial 3

## La parte de desarollo de las preguntas 1, 2, 3 y 5 estan en el archivo p1_a_p2_a_p3_p5.pdf. Referirse a este para las de respuestas de desarrollo.

## Para la pregunta 1, se pude probar usando client.py

Client.py contiene la evaluacion en DFS y BFS implementando Cola y Pila, definidas en Secuiencia.py.

Al correr el cliente, se imprimira el grafo y las evaluaciones. Los nodos explorados se cuentan a partir del incial e incluyendo al ultimo, tomando en cuenta todos los nodos sobre los que paso el algoritmo.

## Para la parte en codigo de la pregunta 2

El inciso (i) de la pregunta 2 esta implementado en dot_vector_concurrent.hs. Al correr el main, se hara un producto entre el vector [1,2,3] y el vector [4,5,6], obteniendo el resultado del producto punto. Si se quiere probar otros vectores con otras dimensiones, cambiarlo dentro del archivo.
El inciso (ii) de la pregunta 2 esta implementado en file_count_concurrent.hs
Correr con ghci seguido del llamado al main. 
ES NECESARIO CORRER LA TERMINAL CON PERMISOS DE ADMINISTRADOR PARA QUE file_count_concurrent.hs FUNCIONE. (Necesario en Windows, no fue probado en Linux.)

## Pregunta 3: Respuesta dentro de p1_a_p2_a_p3_p5.pdf

## Pregunta 4

Para la pregunta 4, se pueden correr las prubeas con:

coverage run -m pytest

Seguido de:

coverage report

para obtener el reporte.

El uso del codigo es mediante 

py Client.py

## Pregunta 5: Respuesta dentro de p1_a_p2_a_p3_p5.pdf

## Pregunta 6

Con toda la honestidad del mundo, el codigo solo puede usar la funcion DEF correctamente.

Es NECESARIO para que funcione que los parametros dentro de parentizacion no tengan espacios en blanco.

padre(a, b) <- No funciona
padre(a,b) <- Funciona

Correr con py prolog_sub.py
