from exp_parser import Parser


def test_PRE1():
    manejador = Parser("PRE","- 9 8" )
    assert manejador.parse() == 1

def test_PRE2():
    manejador = Parser("PRE","+ 5 4" )
    assert manejador.parse() == 9

def test_PRE3():
    manejador = Parser("PRE","* 4 4" )
    assert manejador.parse() == 16    

def test_PRE4():
    manejador = Parser("PRE","/ 4 4" )
    assert manejador.parse() == 1    

def test_POST1():
    manejador = Parser("POST","98-" )
    assert manejador.parse() == 1    

def test_POST2():
    manejador = Parser("POST","54+" )
    assert manejador.parse() ==  9    

def test_POST3():
    manejador = Parser("POST","44*" )
    assert manejador.parse() ==  16   

def test_POST4():
    manejador = Parser("POST","44/" )
    assert manejador.parse() ==  1   

def test_MOSTRAR1():
    manejador = Parser("PRE","+*+3457" )
    assert manejador.mostrar() == "(3 + 4) * 5 + 7"

def test_MOSTRAR2():
    manejador = Parser("POST","83-844+*+" )
    assert manejador.mostrar() == "8 - 3 + 8 * (4 + 4)"


      