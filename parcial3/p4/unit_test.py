from Manejador import Manejador

manejador =  Manejador()

def test_def_clase1():
    
    a = manejador.def_clase("A",None,["a,b,c"])
    b = "\nClase A creada." 

    assert manejador.tabla["A"].nombre == "A"
    assert manejador.tabla["A"].super == None
    assert manejador.tabla["A"].metodos == ["a,b,c"]
    assert a == b
    

def test_define_copy():
    
    a = manejador.def_clase("A",None,["a,b,c"])
    b = "\nA ya se encuentra definida."

    assert a == b

def test_def_clase2():
    
    a = manejador.def_clase("B","A",None)
    b = (f"\nClase B que hereda de A creada.")   

    assert a == b

def test_define_dupmet():
    
    a = manejador.def_clase("C","B",["c","c"])
    b = "\nNo pueden haber metodos duplicados en la lista de metodos." 

    assert a == b

def test_def_clase3():
    
    a = manejador.def_clase("C","B",["d"])
    b = "\nClase C que hereda de B creada."

    assert a == b

def test_describir1():

    a = manejador.describir("Z")
    b = "\nClase Z no se encuentra definida"

    assert a == b

def test_describir2():

    a = manejador.describir("A")
    b = "\na,b,c -> A :: a,b,c\n"

    assert a == b