# importar BuddySystem
from buddy_system import Buddy_System

system = Buddy_System(32)

# RESERVAR test
def test_RESERVAR1():
    assert system.reservar(1, 'Reserva0') == "Se ha alojado la memoria en el bloque (0, 0) bajo el nombre: Reserva0"

def test_RESERVAR_error1():
    assert system.reservar(2, 'Reserva0') == "El nombre introducido se encuentra ocupado."

def test_RESERVAR_error2():
    assert system.reservar(-1, 'Reserva1') == "Se debe introducir un entero positivo como parametro de cantidad de memoria."

def test_RESERVAR2():
    assert system.reservar(2, 'Reserva2') == "Se ha alojado la memoria en el bloque (2, 3) bajo el nombre: Reserva2"

def test_RESERVAR3():
    assert system.reservar(1, 'Reserva3') == "Se ha alojado la memoria en el bloque (1, 1) bajo el nombre: Reserva3"
    
def test_RESERVAR4():
    assert system.reservar(4, 'Reserva4') == "Se ha alojado la memoria en el bloque (4, 7) bajo el nombre: Reserva4"

def test_RESERVAR5():
    assert system.reservar(4, 'Reserva5') == "Se ha alojado la memoria en el bloque (8, 11) bajo el nombre: Reserva5"

def test_RESERVAR6():
    assert system.reservar(2, 'Reserva6') == "Se ha alojado la memoria en el bloque (12, 13) bajo el nombre: Reserva6"

def test_RESERVAR7():
    assert system.reservar(2, 'Reserva7') == "Se ha alojado la memoria en el bloque (14, 15) bajo el nombre: Reserva7"

def test_RESERVAR8():
    assert system.reservar(10, 'Reserva8') == "Se ha alojado la memoria en el bloque (16, 31) bajo el nombre: Reserva8"

def test_RESERVAR_error3():
    assert system.reservar(10, 'Reserva9') == "No hay memoria libre suficiente para alojar al bloque"

def test_RESERVAR_error4():
    assert system.reservar(100, 'Reserva9') == "No hay memoria libre suficiente para alojar al bloque"

def test_RESERVAR_error5():
    assert system.reservar(1000, 'Reserva9') == "No hay memoria libre suficiente para alojar al bloque"

# LIBERAR test
def test_LIBERAR1():
    assert system.liberar('Reserva4') == "Se ha liberado de memoria: Reserva4, alojado en bloque (4, 7)"

def test_RESERVAR_Realocation1():
    assert system.reservar(2, 'Realocation1') == "Se ha alojado la memoria en el bloque (4, 5) bajo el nombre: Realocation1"

def test_RESERVAR_Realocation2():
    assert system.reservar(2, 'Realocation2') == "Se ha alojado la memoria en el bloque (6, 7) bajo el nombre: Realocation2"

def test_LIBERAR_error():
    assert system.liberar('ERROR') == "No existe el bloque 'ERROR' alojado en memoria."

def test_LIBERAR2():
    assert system.liberar('Reserva8') == "Se ha liberado de memoria: Reserva8, alojado en bloque (16, 31)"

def test_RESERVAR_Realocation3():
    assert system.reservar(10, 'Realocation3') == "Se ha alojado la memoria en el bloque (16, 31) bajo el nombre: Realocation3"

# MOSTRAR test
def test_MOSTRAR():
    assert system.mostrar()