import math
from itertools import permutations

class Manejador(object):

    def __init__(self):

        self.atomos = {}
        self.struct = {}
        self.union = {}

    def handle_atomico(self, args):

        try:
            nombre = args[1]
            representacion = args[2]
            alineacion = args[3]
        except:
            print("Error en los argumentos recibidos")
            return

        # Definimos el tipo atomico
        if(  nombre in self.union or nombre in self.atomos or nombre in self.struct  ):
            print("El Nombre ya esta definido en memoria\nAccion Ignorada")
        else:
            self.atomos[nombre] = [representacion, alineacion]
            print("Atomico agregado.")

    def handle_struct(self, args):

        tipos = []
        try:
            nombre = args[1]
            tipos = args[2:]
        except IndexError:
            print("Error en los argumentos recibidos")
            return

        # Se almacena en memoria el struct
        if( nombre in self.union or nombre in self.atomos or nombre in self.struct ):
            print("El Nombre ya esta definido en memoria\nAccion Ignorada")
        else:
            if(not all(i in self.atomos for i in tipos)):
                print("Alguno de los tipos atomicos introducidos no estan aun registrados")
            else:
                self.struct[nombre] = tipos
            print("Struct agregado.")

    def handle_union(self, args):

        tipos = []
        try:
            nombre = args[1]
            tipos = args[2:]
        except IndexError:
            print("Error en los argumentos recibidos")
            return

        # Se almacena en memoria el union
        if( nombre in self.union or nombre in self.atomos or nombre in self.struct ):
            print("El Nombre ya esta definido en memoria\nAccion Ignorada")
        else:
            if not (all(i in self.atomos for i in tipos) or any(i in self.struct for i in tipos)):
                print("Alguno de los tipos atomicos introducidos no estan aun registrados")
            else:
                atomos_tipos = [tipo for tipo in tipos if tipo in self.atomos]
                struct_tipos = [tipo for tipo in tipos if tipo in self.struct]
                struct_values = []
                for value in struct_tipos:
                    for i in self.struct[value]:
                        struct_values.append(i)
                max_atomos = max([int(self.atomos[tipo][0]) for tipo in atomos_tipos]) if atomos_tipos else 0
                max_struct = max([int(self.atomos[tipo][0]) for tipo in struct_values]) if struct_tipos else 0
                representacion = max(max_atomos, max_struct)
                alineacion = self.lcm(atomos_tipos,struct_values)
                if representacion > -1:
                    self.union[nombre] = [representacion, alineacion]
                print("Union agregada.")


    def lcm(self, tipos_atom, tipos_struct):
        mcm = 1
        for a in (int(self.atomos[i][1]) for i in tipos_atom):
            mcm *= a // math.gcd(mcm, a)
        for a in (int(self.atomos[i][1]) for i in tipos_struct):
            mcm *= a // math.gcd(mcm, a)   
        return mcm

    def describir(self, argumentos):

        # Separamos los argumentos
        nombre = ""
        try:
            aux = argumentos.split(' ')
            nombre = aux[0]
        except IndexError:
            print("Error en los argumentos recibidos")
        
        if(nombre in self.atomos):
            self.describir_tipo_atomico(nombre)
        elif( nombre in self.struct ):
            self.describir_tipo_struct(nombre)
        elif( nombre in self.union ):
            self.describir_tipo_union(nombre)
        else:
            print("Tipo de dato no Definido")


    def describir_tipo_atomico(self,nombre):
        
        print("TIPO ATOMICO SIN EMPAQUETADO")
        print("Tamaño    Alineacion    Bytes desperdiciados")
        print(self.atomos[nombre][0],"\t\t", self.atomos[nombre][1],"\t\t", 0)

        print("TIPO ATOMICO EMPAQUETADO")
        print("Tamaño    Alineacion    Bytes desperdiciados")
        print(self.atomos[nombre][0],"\t\t", self.atomos[nombre][1],"\t\t", 0)

        print("TIPO ATOMICO REORDENADO")
        print("Tamaño    Alineacion    Bytes desperdiciados")
        print(self.atomos[nombre][0],"\t\t", self.atomos[nombre][1],"\t\t", 0)


    def describir_tipo_struct(self,nombre):
        self.memoria_struct_sin_empaquetar(nombre)
        self.memoria_struct_empaquetando(nombre)
        self.memoria_struct_reordenando(nombre)

    def describir_tipo_union(self, nombre):
        print("TIPO UNION SIN EMPAQUETADO")
        print("Tamaño    Alineacion    Bytes desperdiciados")
        print(self.union[nombre][0],"\t\t", self.union[nombre][1],"\t\t", 0)

        print("TIPO UNION EMPAQUETADO")
        print("Tamaño    Alineacion    Bytes desperdiciados")
        print(self.union[nombre][0],"\t\t", self.union[nombre][1],"\t\t", 0)

        print("TIPO UNION REORDENADO")
        print("Tamaño    Alineacion    Bytes desperdiciados")
        print(self.union[nombre][0],"\t\t", self.union[nombre][1],"\t\t", 0)

    def memoria_struct_sin_empaquetar(self, nombre, to_use = False):

        if to_use == True:
            atomicos = nombre
        else:
            atomicos = self.struct[nombre]

        memoria_ocupada = 0
        desperdicio = 0

        
        for i in atomicos:
            while memoria_ocupada % int(self.atomos[i][1]) != 0:
                memoria_ocupada += 1
            for i in range(int(self.atomos[i][0])):
                memoria_ocupada += 1
                desperdicio += 1

        desperdicio = memoria_ocupada - desperdicio

        alineacion = memoria_ocupada + (4 - memoria_ocupada % 4)


        if to_use == True:
            return memoria_ocupada, alineacion, desperdicio
        else:
            print("TIPO STRUCT SIN EMPAQUETADO")
            print("Tamaño    Alineacion    Bytes desperdiciados")
            print(memoria_ocupada, "  ", alineacion,"  ", desperdicio)



    def memoria_struct_empaquetando(self, nombre, to_use = False):

        memoria_ocupada = 0

        atomicos = self.struct[nombre]
        for i in atomicos:
            memoria_ocupada += int(self.atomos[i][0])
                

        alineacion = memoria_ocupada + (4 - memoria_ocupada % 4)

        if to_use == True:
            return memoria_ocupada, alineacion, 0
        else:
            print("TIPO STRUCT EMPAQUETADO")
            print("Tamaño    Alineacion    Bytes desperdiciados")
            print(memoria_ocupada, "  ", alineacion,"  ", "0")


    def memoria_struct_reordenando(self, nombre, to_use = False):
        
        atomicos = self.struct[nombre]

        todos_tipos = list(permutations(atomicos, len(atomicos)))

        memoria_ocupada = float('inf')
        alineacion = float('inf')
        desperdicio = float('inf')

        for t in todos_tipos:
            [curr_ocupado, curr_alineacion, curr_desperdicio] = self.memoria_struct_sin_empaquetar(t,to_use=True)

            if curr_ocupado < memoria_ocupada:
                memoria_ocupada = curr_ocupado
                alineacion = curr_alineacion
                desperdicio = curr_desperdicio

        if to_use == True:
            return memoria_ocupada, alineacion, desperdicio
        else:
            print("TIPO STRUCT REORDENADO")
            print("Tamaño    Alineacion    Bytes desperdiciados")
            print(memoria_ocupada, "  ", alineacion,"  ", desperdicio)
