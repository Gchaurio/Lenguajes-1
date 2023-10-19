# Lenguajes-1
Para correr los scripts de go, se debe tener instalado Go(Golang) y usar el comando "go run":

go run ./p1_b1.go hola 3
go run ./p1_b2.go matriz.txt

Las preguntas 4 y 5 cuentan con clientes ejecutables.
El cliente del buddy system debe ser inicializado con el argumento de cantidad de memoria.

Para correr las pruebas unitarias de las preguntas 3, 4 y 5:

coverage run -m pytest
coverage report
