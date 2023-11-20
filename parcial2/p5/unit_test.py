from manejador import Manejador

manejador = Manejador()

def test_empty_add_atom():

    manejador.handle_atomico("")

    assert "Error en los argumentos recibidos"

def test_empty_add_struc():

    manejador.handle_struct("")

    assert "Error en los argumentos recibidos"

def test_empty_add_union():

    manejador.handle_union("")

    assert "Error en los argumentos recibidos"

def test_correct_add_atom():

    manejador.handle_atomico("char 3 2")

    assert "Atomico agregado."


def test_duplicate_add():

    manejador.handle_atomico("char 3 2")

    assert "El Nombre ya esta definido en memoria\nAccion Ignorada"

def test_extra_args():

    manejador.handle_atomico("char2 3 2 5")
    
    assert "Error en los argumentos recibidos"

def test_correct_add2_atom():

    manejador.handle_atomico("char2 5 2")

    assert "Atomico agregado."

def test_incorrect_add_struc():

    manejador.handle_struct("struct char1 char2")

    assert "Alguno de los tipos atomicos introducidos no estan aun registrados"

def test_correct_add_struc():

    manejador.handle_struct("struct char char2")

    assert "Struct agregado."

def test_repeat_add_struc():

    manejador.handle_struct("struct char char2")

    assert "El Nombre ya esta definido en memoria\nAccion Ignorada"


def test_incorrect_add_union():

    manejador.handle_struct("union char10 struct char2")

    assert "Alguno de los tipos atomicos introducidos no estan aun registrados"

def test_correct_add_union():

    manejador.handle_struct("union char struct char2")

    assert "Union agregada."

def test_repeat_add_union():

    manejador.handle_struct("union char struct char2")

    assert "El Nombre ya esta definido en memoria\nAccion Ignorada"

def test_describir_empty():

    manejador.describir("")

    assert "Error en los argumentos recibidos"

def test_describir_non_exist():

    manejador.describir("charro")

    assert "Tipo de dato no Definido"

def test_mostrar_atomo():

    manejador.describir("char")

    assert "TIPO ATOMICO SIN EMPAQUETADO"
    assert "Tamaño    Alineacion    Bytes desperdiciados"
    assert "3\t\t2""\t\t0"
    assert "TIPO ATOMICO EMPAQUETADO"
    assert "Tamaño    Alineacion    Bytes desperdiciados"
    assert "3\t\t2""\t\t0"
    assert "TIPO ATOMICO REORDENADO"
    assert "Tamaño    Alineacion    Bytes desperdiciados"
    assert "3\t\t2""\t\t0"

def test_mostrar_atomo():

    manejador.describir("char2")

    assert "TIPO ATOMICO SIN EMPAQUETADO"
    assert "Tamaño    Alineacion    Bytes desperdiciados"
    assert "5\t\t2""\t\t0"
    assert "TIPO ATOMICO EMPAQUETADO"
    assert "Tamaño    Alineacion    Bytes desperdiciados"
    assert "5\t\t2""\t\t0"
    assert "TIPO ATOMICO REORDENADO"
    assert "Tamaño    Alineacion    Bytes desperdiciados"
    assert "5\t\t2""\t\t0"

def test_mostrar_struc():

    manejador.describir("struct")

    assert "TIPO STRUCT SIN EMPAQUETADO"
    assert "Tamaño    Alineacion    Bytes desperdiciados"
    assert "9\t\t12""\t\t1"
    assert "TIPO STRUCT EMPAQUETADO"
    assert "Tamaño    Alineacion    Bytes desperdiciados"
    assert "8\t\t12""\t\t0"
    assert "TIPO STRUCT REORDENADO"
    assert "Tamaño    Alineacion    Bytes desperdiciados"
    assert "9\t\t12""\t\t1"

def test_mostrar_union():

    manejador.describir("union")

    assert "TIPO UNION SIN EMPAQUETADO"
    assert "Tamaño    Alineacion    Bytes desperdiciados"
    assert "5\t\t2""\t\t0"
    assert "TIPO UNION EMPAQUETADO"
    assert "Tamaño    Alineacion    Bytes desperdiciados"
    assert "5\t\t2""\t\t0"
    assert "TIPO UNION REORDENADO"
    assert "Tamaño    Alineacion    Bytes desperdiciados"
    assert "5\t\t2""\t\t0"

    