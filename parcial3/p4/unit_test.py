from VM import VM

vm =  VM()

def test_define_class1():
    
    a = vm.define_class("A",None,["a,b,c"])
    b = "\nClase A creada." 

    assert vm.tabla_de_simbolos["A"].nombre == "A"
    assert vm.tabla_de_simbolos["A"].super_clase == None
    assert vm.tabla_de_simbolos["A"].metodos == ["a,b,c"]
    assert a == b
    

def test_define_copy():
    
    a = vm.define_class("A",None,["a,b,c"])
    b = "\nA ya se encuentra definida."

    assert a == b

def test_define_class2():
    
    a = vm.define_class("B","A",None)
    b = (f"\nClase B que hereda de A creada.")   

    assert a == b

def test_define_dupmet():
    
    a = vm.define_class("C","B",["c","c"])
    b = "\nNo pueden haber metodos duplicados en la lista de metodos." 

    assert a == b

def test_define_class3():
    
    a = vm.define_class("C","B",["d"])
    b = "\nClase C que hereda de B creada."

    assert a == b

def test_describir1():

    a = vm.describir("Z")
    b = "\nLa clase Z no se encuentra definida"

    assert a == b

def test_describir2():

    a = vm.describir("A")
    b = "\na,b,c -> A :: a,b,c\n"

    assert a == b