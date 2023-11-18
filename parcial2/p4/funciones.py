def f_recur(n: int) -> int:
    if 0 <= n < 36:
        return n
    else:
        return sum([f_recur(n - 6* i) for i in range(1, 7)])
    

def f_cola(n:int) -> int:

    return f_aux(n, [i for i in range(0, 36)], 35)
    
def f_aux(n: int, x: list, i: int) -> int:

    if 0 <= n < 36:
        return x[n]
    
    elif n == i:

        return sum([x[35 - i*6] for i in range(1, 7)])
    
    else:

        to_add = sum([x[35 - i*6] for i in range(1, 7)])
        x[:-1] = x[1:]
        x.append(to_add)
        
        return f_aux(n, x, i+1)
    
def f_iter(n:int):

    i = 35
    x = [i for i in range(0, 36)]

    if 0 <= n < 36:
        return n

    while n != i:    

        to_add = sum([x[35 - i*6] for i in range(1, 7)])
        x[:-1] = x[1:]
        x.append(to_add)
        i += 1

    return sum([x[35 - i*6] for i in range(1, 7)])
