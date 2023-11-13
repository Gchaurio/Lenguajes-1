class Programa:
    def __init__(self, nombre, lenguaje):
        self.nombre = nombre
        self.lenguaje = lenguaje

class Interprete:
    def __init__(self, lenguaje_base, lenguaje):
        self.lenguaje_base = lenguaje_base
        self.lenguaje = lenguaje

class Traductor:
    def __init__(self, lenguaje_base, lenguaje_origen, lenguaje_destino):
        self.lenguaje_base = lenguaje_base
        self.lenguaje_origen = lenguaje_origen
        self.lenguaje_destino = lenguaje_destino

programas = []
interpretes = []
traductores = []

def main():
    while True:
        accion = input("Ingrese una acción (DEFINIR, EJECUTABLE, SALIR): ")
        if "DEFINIR" in accion.split(" "):
            arg1 = accion.split(" ")[1].strip()
            arg2 = accion.split(" ")[2].strip()
            arg3 = accion.split(" ")[3].strip()
            if arg1 == "PROGRAMA":
                nombre = arg2
                lenguaje =  arg3
                if nombre in list(programa.nombre for programa in programas):
                    print("Error: el programa '{}' ya existe".format(nombre))
                else:
                    programas.append(Programa(nombre, lenguaje))
                    print("Se definió el programa '{}', ejecutable en '{}'".format(nombre, lenguaje))
            elif arg1 == "INTERPRETE":
                lenguaje_base = arg2
                lenguaje = arg3
                if any((lenguaje_base == interprete.lenguaje_base) and (lenguaje == interprete.lenguaje) for interprete in interpretes):
                    print("Error: el intérprete para '{}' ya existe".format(lenguaje))
                else:
                    interpretes.append(Interprete(lenguaje_base, lenguaje))
                    print("Se definió un intérprete para '{}', escrito en '{}'".format(lenguaje, lenguaje_base))
            elif arg1 == "TRADUCTOR":
                lenguaje_base = arg2
                lenguaje_origen = arg3
                lenguaje_destino = accion.split(" ")[4].strip()
                if any((lenguaje_base == traductor.lenguaje_base) and (lenguaje_origen == traductor.lenguaje_origen) and (lenguaje_destino == traductor.lenguaje_destino) for traductor in traductores):
                    print("Error: el traductor de '{}' a '{}' ya existe".format(lenguaje_origen, lenguaje_destino))
                else:
                    traductores.append(Traductor(lenguaje_base, lenguaje_origen, lenguaje_destino))
                    print("Se definió un traductor de '{}' hacia '{}', escrito en '{}'".format(lenguaje_origen, lenguaje_destino, lenguaje_base))
        elif "EJECUTABLE" in accion.split(" "):
            nombre = accion.split(" ")[1].strip()
            if nombre in list(programa.nombre for programa in programas):
                programa = next(filter(lambda objeto: objeto.nombre == nombre, programas))
                if lenguaje == "LOCAL":
                    print("Si, es posible ejecutar el programa '{}'".format(nombre))
                elif ejecutable(interpretes, traductores, programa.lenguaje):
                    print("Si, es posible ejecutar el programa '{}'".format(nombre))
                else:
                    print("No es posible ejecutar el programa '{}'".format(nombre))
            else:
                print("Error: el programa '{}' no existe".format(nombre))
        elif accion == "SALIR":
            break

# Determina si un programa es ejecutable
def ejecutable(interpretes, traductores, lenguaje):
    """
    Devuelve True si el programa con el nombre dado se puede ejecutar, False en caso contrario.

    Args:
        name: El nombre del programa.

    Returns:
        True si el programa se puede ejecutar, False en caso contrario.
    """

    # Conjunto de lenguajes desde los que se puede ejecutar el programa.
    lenguajes_ejecutables = set()

    # Agregamos el lenguaje local a la lista de lenguajes desde los que se puede ejecutar el programa.
    lenguajes_ejecutables.add("LOCAL")

    # Mientras haya lenguajes desde los que se pueda ejecutar el programa, continuamos iterando.
    while lenguajes_ejecutables:
        # Conjunto de lenguajes desde los que se podrá ejecutar el programa en la siguiente iteración.
        nuevos_lenguajes_ejecutables = lenguajes_ejecutables

        # Iteramos sobre los intérpretes.
        for interpretador in interpretes:
            # Si el lenguaje base del intérprete está en la lista de lenguajes desde los que se puede ejecutar el programa,
            # agregamos el lenguaje del intérprete a la lista de lenguajes desde los que se podrá ejecutar el programa en la siguiente iteración.
            if interpretador.lenguaje_base in lenguajes_ejecutables:
                nuevos_lenguajes_ejecutables.add(interpretador.lenguaje)

        # Iteramos sobre los traductores.
        for traductor in traductores:
            # Si el lenguaje base del traductor y el lenguaje destino del traductor están en la lista de lenguajes desde los que se puede ejecutar el programa,
            # agregamos el lenguaje origen del traductor a la lista de lenguajes desde los que se podrá ejecutar el programa en la siguiente iteración.
            if traductor.lenguaje_base in lenguajes_ejecutables and traductor.lenguaje_destino in lenguajes_ejecutables:
                nuevos_lenguajes_ejecutables.add(traductor.lenguaje_origen)

        # Si la lista de lenguajes desde los que se puede ejecutar el programa no ha cambiado, entonces hemos encontrado un punto fijo.
        if nuevos_lenguajes_ejecutables == lenguajes_ejecutables:
            break

        # Actualizamos la lista de lenguajes desde los que se puede ejecutar el programa.
        lenguajes_ejecutables = nuevos_lenguajes_ejecutables | lenguajes_ejecutables

    # Devolvemos True si el programa está escrito en un lenguaje desde el que se puede ejecutar, False en caso contrario.
    return lenguaje in lenguajes_ejecutables


if __name__ == "__main__":
    main()