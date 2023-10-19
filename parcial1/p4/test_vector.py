from vector import Vector3D

# Se inicializan los vectores. 
a = Vector3D(1, 2, 3)
b = Vector3D(4, -5, 6)
c = Vector3D(-2, -3, -4)

# Se crean dos vectores con valores float para probar las operaciones.
vector_float = Vector3D(1.5, 2.5, 3.5)
neg_float = Vector3D(-1.5, -1.5, -1.5)

# Se prueba cada operando con flotantes, enteros y entre vectores con numeros flotantes, enteros, tanto positivos
# como negativos
def test_suma_vectores():
    test = a + b
    assert test.x == 5
    assert test.y == -3
    assert test.z == 9

def test_suma_vectores_float():
    test = vector_float + vector_float
    assert test.x == 3.0
    assert test.y == 5.0
    assert test.z == 7.0

def test_suma_vectores_float_neg():
    test = neg_float + neg_float 
    assert test.x == -3.0
    assert test.y == -3.0
    assert test.z == -3.0

def test_suma_vectores_float_mix():
    test = vector_float + neg_float
    assert test.x == 0.0
    assert test.y == 1.0
    assert test.z == 2.0

def test_suma_vector_float():
    test = a + 5.5 
    assert test.x == 6.5
    assert test.y == 7.5
    assert test.z == 8.5

def test_suma_vector_int():
    test = a + 8 
    assert test.x == 9
    assert test.y == 10
    assert test.z == 11

def test_resta_vectores():
    test = a - b 
    assert test.x == -3
    assert test.y == 7
    assert test.z == -3

def test_resta_vectores_float():
    test = vector_float - vector_float
    assert test.x == 0.0
    assert test.y == 0.0
    assert test.z == 0.0

def test_resta_vectores_float_neg():
    test = neg_float - neg_float
    assert test.x == 0.0
    assert test.y == 0.0
    assert test.z == 0.0

def test_resta_vectores_float_mix():
    test = vector_float - neg_float
    assert test.x == 3.0
    assert test.y == 4.0
    assert test.z == 5.0

def test_resta_vector_float():
    test = a - 5.5
    assert test.x == -4.5
    assert test.y == -3.5
    assert test.z == -2.5

def test_resta_vector_int():
    test = a - 8 
    assert test.x == -7
    assert test.y == -6
    assert test.z == -5

def test_multiplicacion_vectores():
    test = a * b 
    assert test.x == 27
    assert test.y == 6
    assert test.z == -13

def test_multiplicacion_vectores_float():
    test = vector_float * neg_float
    assert test.x == 1.5
    assert test.y == -3.0
    assert test.z == 1.5

def test_multiplicacion_vectores_mix():
    test = a * vector_float
    assert test.x == -0.5
    assert test.y == 1.0
    assert test.z == -0.5

def test_multiplicacion_vector_int():
    test = a * 4 
    assert test.x == 4
    assert test.y == 8
    assert test.z == 12

def test_multiplicacion_vector_float():
    test = a * 3.5 
    assert test.x == 3.5
    assert test.y == 7.0
    assert test.z == 10.5

def test_mod_vector():
    assert a % b == 12

def test_mod_float():
    assert vector_float % neg_float == -11.25

def test_mod_mix():
    assert a % vector_float == 17.0

# Operaciones definidas en el enunciado
def test_operacion1():
    test = a * b + c
    assert test.x == 25
    assert test.y == 3
    assert test.z == -17

def test_operacion2():
    test = (b + b) * (c - a) 
    assert test.x == 130
    assert test.y == 20
    assert test.z == -70

def test_operacion3():
    assert a % (c * b) == 20

def test_operacion4():
    result = a * 3.0 + b&b
    assert result == 10.63014581273465

def test_operacion5():
    test = (b + b) * (c % a) 
    assert test.x == -160
    assert test.y == 200
    assert test.z == -240

