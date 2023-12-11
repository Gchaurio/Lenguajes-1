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
            return f"La clase \"{clase}\" ya se encuentra definida."
        if superclase and not superclase in self.tabla_de_simbolos:
            return (f"La clase \"{superclase}\" no se encuentra definida. No puede ser usada como superclase si no se ha definido.")
        if len(metodos) != len(set(metodos)):
            return (f"Hay elementos duplicados en la lista de metodos:\n{metodos}\nNo pueden haber metodos duplicados.")
        if not superclase:
            self.tabla_de_simbolos[clase] = Tipo(clase, None, metodos)
            return f"Se ha creado la clase \"{clase}\"." 
        else:
            self.tabla_de_simbolos[clase] = Tipo(
                clase, self.tabla_de_simbolos[superclase], metodos)   
            return f"Se ha creado la clase \"{clase}\" que hereda de \"{superclase}\"."             
                    

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

        out = ''
        for metodo, clase in lista_de_metodos_con_tipo:
                out += f'{metodo} -> {clase} :: {metodo}\n'
        return out
    


        








