class Tipo(object):
    nombre: str
    super_clase: object
    metodos: list[str]

    def __str__(self) -> str:
        if self.super_clase:
            return f'<{self.nombre}> : <{self.super_clase.nombre}>'
        else:
            return f'<{self.nombre}>'

    def __repr__(self) -> str:
        return self.__str__()

class VM(object):
    
    def __init__(self):
        self.tabla_de_simbolos: dict[str, Tipo] = {}
        

    def define_class(self, clase: str, superclase:str, metodos: list[str]):

        if clase in self.tabla_de_simbolos:
            print(clase_ya_definida(clase))
            return
        if superclase and not superclase in self.tabla_de_simbolos:
            print(superclase_no_definida(superclase))
            return
        if len(metodos) != len(set(metodos)):
            print(elementos_duplicados_en_lista_de_metodos(metodos))
            return
        if not superclase:
            self.tabla_de_simbolos[clase] = Tipo(clase, None, metodos)
            print(clase_creada(clase))
        else:
            self.tabla_de_simbolos[clase] = Tipo(
                clase, self.tabla_de_simbolos[superclase], metodos)                
            print(clase_creada(clase, superclase))

    def describir(self, clase:str):

        if not clase in self.tabla_de_simbolos:
            print(f"La clase {clase} no se encuentra definida")
            return

        lista_de_metodos_con_tipo: tuple(str, str) = []
        historial_de_metodos: list(str) = []
        clase: Tipo = self.tabla_de_simbolos[clase]
        while clase:
            lista_de_metodos_de_clase = []
            for metodo in clase.metodos:
                if metodo in historial_de_metodos:
                    continue

                lista_de_metodos_de_clase.append((metodo, clase.nombre))
                historial_de_metodos.append(metodo)
            lista_de_metodos_con_tipo[0:0] = lista_de_metodos_de_clase
            clase = clase.super_clase
            
        print(mostrar_metodos_y_clases(lista_de_metodos_con_tipo), end="")

def clase_ya_definida(clase:str):
    return f"La clase \"{clase}\" ya se encuentra definida."

def superclase_no_definida(superclase:str):
    return (f"La clase \"{superclase}\" no se encuentra definida."
        " No puede ser usada como superclase si no se ha definido.")

def elementos_duplicados_en_lista_de_metodos(metodos: list[str]):
    return (f"Hay elementos duplicados en la lista de metodos:\n{metodos}"
        "\nNo pueden haber metodos duplicados.")

def clase_creada(clase:str , superclase:str=None):
    if superclase:
        return f"Se ha creado la clase \"{clase}\" que hereda de \"{superclase}\"."
    else:
        return f"Se ha creado la clase \"{clase}\"."

def mostrar_metodos_y_clases(lista_de_metodos_y_tipos: list[tuple[str, str]]):
    out = ''
    for metodo, clase in lista_de_metodos_y_tipos:
            out += f'{metodo} -> {clase} :: {metodo}\n'
    return out


        








