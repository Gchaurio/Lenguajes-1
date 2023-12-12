class Tipo(object):
    
    def __init__(self, nombre, super_clase, metodos):
        self.nombre = nombre
        self.super_clase = super_clase
        self.metodos = metodos

class VM(object):
    
    def __init__(self):
        self.tabla_de_simbolos: dict[str, Tipo] = {}
        
    def define_class(self, clase: str, superclase:str, metodos: list[str]):

        if clase in self.tabla_de_simbolos:
            return (f"\n{clase} ya se encuentra definida.")
        if superclase and not superclase in self.tabla_de_simbolos:
            return (f"\n{superclase} no se encuentra definida. Debe definirse para usarse como superclase.")
        if metodos != None and len(metodos) != len(set(metodos)):
            return (f"\nNo pueden haber metodos duplicados en la lista de metodos.")
        if not superclase:
            self.tabla_de_simbolos[clase] = Tipo(clase, None, metodos)
            return (f"\nClase {clase} creada.") 
        if metodos == None:
            self.tabla_de_simbolos[clase] = Tipo(self.tabla_de_simbolos[superclase].nombre, self.tabla_de_simbolos[superclase], self.tabla_de_simbolos[superclase].metodos)   
            return (f"\nClase {clase} que hereda de {superclase} creada.")      
        else:
            self.tabla_de_simbolos[clase] = Tipo(clase, self.tabla_de_simbolos[superclase], metodos)   
            return (f"\nClase {clase} que hereda de {superclase} creada.")             
                    

    def describir(self, clase:str):

        if not clase in self.tabla_de_simbolos:
            return (f"\nLa clase {clase} no se encuentra definida")

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

        out = '\n'
        for metodo, clase in lista_de_metodos_con_tipo:
                out += f'{metodo} -> {clase} :: {metodo}\n'
        return out
    


        








