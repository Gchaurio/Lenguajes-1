class Tipo(object):
    
    def __init__(self, nombre, super, metodos):
        self.nombre = nombre
        self.super = super
        self.metodos = metodos

class Manejador(object):
    
    def __init__(self):
        self.tabla: dict[str, Tipo] = {}
        
    def def_clase(self, clase: str, super:str, metodos: list[str]):

        if clase in self.tabla:
            return (f"\n{clase} ya se encuentra definida.")
        if super and not super in self.tabla:
            return (f"\n{super} no se encuentra definida. Debe definirse para usarse como Super Clase.")
        if metodos != None and len(metodos) != len(set(metodos)):
            return (f"\nNo pueden haber metodos duplicados en la lista de metodos.")
        if not super:
            self.tabla[clase] = Tipo(clase, None, metodos)
            return (f"\nClase {clase} creada.") 
        if metodos == None:
            self.tabla[clase] = Tipo(self.tabla[super].nombre, self.tabla[super], self.tabla[super].metodos)   
            return (f"\nClase {clase} que hereda de {super} creada.")      
        else:
            self.tabla[clase] = Tipo(clase, self.tabla[super], metodos)   
            return (f"\nClase {clase} que hereda de {super} creada.")                            

    def describir(self, clase:str):

        if not clase in self.tabla:
            return (f"\nClase {clase} no se encuentra definida")

        metodo_clase: tuple(str, str) = []
        metodos: list(str) = []
        clase: Tipo = self.tabla[clase]

        while clase:
            lista_metodo_clase = []
            for metodo in clase.metodos:
                if metodo in metodos:
                    continue
                lista_metodo_clase.append((metodo, clase.nombre))
                metodos.append(metodo)
            metodo_clase[0:0] = lista_metodo_clase
            clase = clase.super

        out = '\n'
        for metodo, clase in metodo_clase:
                out += f'{metodo} -> {clase} :: {metodo}\n'
        return out
    


        








