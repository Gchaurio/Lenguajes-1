# cython : language_level=3

cdef enum Church:
    Cero,
    Suc

cdef Church add(Church x, Church y):
    if x == Cero:
        return y
    return Suc(add(Suc(x), y))

cdef Church mul(Church x, Church y):
    if x == Cero:
        return Cero
    if y == Cero:
        return Cero
    return Suc(mul(Suc(x), Suc(y)))