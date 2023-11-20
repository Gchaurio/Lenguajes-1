# Metodo recursivo
def f_recur(n: int) -> int:

    # Caso base
    if 0 <= n < 36:
        return n
    else:
        # Se aplica recursion
        return sum([f_recur(n - 6* i) for i in range(1, 7)])
    
# Llamado a la funcion de cola
def f_cola(n:int) -> int:

    # Inicializacion de valores 
    return f_aux(n, [i for i in range(0, 36)], 35)
    
def f_aux(n: int, x: list, i: int) -> int:

    # Caso base
    if 0 <= n < 36:
        return x[n]
    
    # Si se ha alcanzado el valor n, se retorna.
    elif n == i:
        return x[35]
    
    # Se calcula el valor de f(i)
    else:
        
        # Calulamos la suma de los valores que nos interesan, lo colocamos al final de la lista. Movemos los valores hacia atras.
        to_add = sum([x[i*6] for i in range(0, 6)])
        x[:-1] = x[1:]
        x[-1] = to_add

     
        # Calulamos el siguiente valor pasando los valores ya calculados. Aqui es donde se implmenta la cola, con los valores almacenados.
        return f_aux(n, x, i+1)

    
def f_iter(n:int):

    # Objetivo
    i = 35
    x = [i for i in range(0, 36)]

    # Caso base
    if 0 <= n < 36:
        return n

    # Mientras no lleguemos al objetivo, iteramos sobre los valores existentes y calculamos los nuevos en un mismo ciclo iterativo
    while n != i:    

        to_add = sum([x[i*6] for i in range(0, 6)])
        x[:-1] = x[1:]
        x[-1] = to_add
        i += 1

    # una vez llegado al valor, devolvemos la suma.
    return x[35]
