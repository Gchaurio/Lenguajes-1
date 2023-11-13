# Material usado de referencia: https://www.geeksforgeeks.org/buddy-memory-allocation-program-set-1-allocation/

import math 
import sys

class Buddy_System(object):
    
    def __init__(self,n: int):
        if n <= 0:
            raise Exception("La cantidad de bloques debe ser un entero positivo.")
        
        # Se define la cantidad de bloques
        self.blocks = math.floor(math.log2(n))

        # Se definen una lista de listas vacias a partir de la cantidad de bloques
        self.free_blocks = [[] for i in range(self.blocks+1)]

        # Se agrega a la lista de mayor tamanaio el bloque inicial
        self.free_blocks[len(self.free_blocks)-1].append(Block(0, 2**self.blocks-1))

        # Se crea el diccionario que almacena los bloques con sus respectivos nombres
        self.ocuppied_blocks = {}

    def reservar(self, amount: int, name: str):
        """
            Reserva memoria para un bloque con el nombre dado.

            Args:
                amount: El tamaño del bloque a reservar.
                name: El nombre del bloque a reservar.

            Returns:
                Un mensaje de confirmación o error.
        """
        if amount <= 0:
            return "Se debe introducir un entero positivo como parametro de cantidad de memoria."
        if name in self.ocuppied_blocks.keys():
            return "El nombre introducido se encuentra ocupado."
        
        try:
            # Encuentra la lista de bloques de tamaño adecuado
            free_blocks_list = self.free_blocks[math.ceil(math.log2(amount))]
        except:
            # De recibir una excepcion, se esta ingresando mas memoria de la que hay por lo que se devuelve el mensaje.
            return f"No hay memoria libre suficiente para alojar al bloque"

        # Si hay bloques libres en la lista, se asigna uno de ellos
        if free_blocks_list:
            block = free_blocks_list.pop(0)
            if block.allocable < amount:
                pass
            else:
                self.ocuppied_blocks[name] = block
                return f"Se ha alojado la memoria en el bloque {block} bajo el nombre: {name}"

        # Si no hay bloques libres en la lista, se busca un bloque de mayor tamaño y se divide hasta que se encuentre uno de tamaño adecuado
        i = 0
        found = False
        while i != len(self.free_blocks):
            if len(self.free_blocks[i])>0:
                found = True
                break
            i += 1

        if found == False:
            return f"No hay memoria libre suficiente para alojar al bloque"

        # Se divide el bloque encontrado hasta que sea del tamaño adecuado
        split = self.free_blocks[i].pop(0)
        while i-1 >= math.ceil(math.log2(amount)):
            slice1, slice2 = split.divide()
            self.free_blocks[i - 1].append(slice2)
            split = slice1
            i -= 1

        self.ocuppied_blocks[name] = split
        return  f"Se ha alojado la memoria en el bloque {split} bajo el nombre: {name}"
    
    def liberar(self, name: str):
        """
            Libera la memoria asignada al bloque con el nombre dado.

            Args:
                name: El nombre del bloque a liberar.

            Returns:
                Un mensaje de confirmación o error.
        """

        # Se busca en la lista de bloques ocupados el que se va a liberar
        to_free = self.ocuppied_blocks.get(name, None)

        # De no encontrarse el nombre, se envia un aviso.
        if not to_free:
            return f"No existe el bloque '{name}' alojado en memoria."

        # De encontrarse, se busca su posicion y se asigna el bloque a la lista de bloques libres
        position = math.ceil(math.log2(to_free.allocable))
        self.free_blocks[position].append(to_free)

        # Eliminar el bloque de la lista de bloques ocupados
        self.ocuppied_blocks.pop(name)

        return f"Se ha liberado de memoria: {name}, alojado en bloque {to_free}"
        
    def mostrar(self):
        """
            Muestra el estado de la memoria.

            Returns:
                Una cadena con el estado de la memoria.
        """

        display = ""

        free_blocks = []
        for blocks in self.free_blocks:
            free_blocks.extend(blocks)

        # Obtener todos los bloques libres y ordenarlos por dirección
        free_blocks.sort(key=lambda x: x.get_init_dir())

        # Imprimir la lista de bloques libres
        display += "Bloques libres:\n"
        for block in free_blocks:
            display += f"{block}\n"

        # Obtener todos los bloques ocupados y ordenarlos por dirección
        ocuppied_blocks = list(self.ocuppied_blocks.values())
        ocuppied_blocks.sort(key=lambda x: x.get_init_dir())


        # Imprimir la lista de bloques ocupados
        display += "\nBloques ocupados:\n"
        for block in ocuppied_blocks:
            display += f"{block}\n"

        # Imprimir la correspondencia nombre: block
        display += "\nLista de Bloques y respectivos nombres ocupados:\n"
        for name, block in self.ocuppied_blocks.items():
            display += f"{name}: {block}\n"

        return display

# Clase Bloque
class Block(object):

    # Se definen las propiedades requeridas
    def __init__(self, init_dir :int, final_dir :int):

        self.init_dir = init_dir
        self.final_dir = final_dir
        self.allocable = final_dir -init_dir + 1

    #F Funcion que devuelve la posicion inicial del bloque
    def get_init_dir(self):
        return self.init_dir
    
    # Funcion que devuelve la posicion final del bloque
    def get_final_dir(self):
        return self.final_dir
    
    # Funcion que divide un bloque
    def divide(self):

        init_half = self.get_init_dir() + ((self.get_final_dir()-self.get_init_dir())//2)
        final_half = self.get_init_dir() + ((self.get_final_dir()-self.get_init_dir() + 1) //2)
        return Block(self.get_init_dir(), init_half), Block(final_half, self.get_final_dir())

    # Se declaran estas funciones para poder representar el objeto como cadena de texto.
    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f'{(self.init_dir,self.final_dir)}'

# Cliente que maneja el programa.
class Client(object):

    def __init__(self, blocks):

        self.buddy_system = Buddy_System(blocks)
        print('Buddy System - Gabriel Chaurio 17-10126\n')
        print('Inputs posibles:\nRESERVAR <cantidad> <nombre>\nLIBERAR <nombre>\nMOSTRAR\nSALIR\n')

    def client(self):
        while True:
            action = input("\nIntroduzca un comando:\n").strip().split(' ')
            if "RESERVAR" in action:
                if len(action) != 3:
                    print('Se han recibido inputs de mas.')
                try:
                    amount = int(action[1])
                    print(self.buddy_system.reservar(amount,action[2]))
                except:
                    print("El valor introducido para cantidad de memoria a reservar, no es un numero.")
            elif "LIBERAR" in action:
                if len(action) != 2:
                    print('Se han recibido inputs de mas.')
                print(self.buddy_system.liberar(action[1]))
            elif "MOSTRAR" in action:
                if len(action) != 1:
                    print('Se han recibido inputs de mas.')
                print(self.buddy_system.mostrar())
            elif "SALIR" in action:
                exit()
            else:
                print("No se ha reconocido el comando")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("\nDebe introducir la cantidad de memoria.")
    else:
        try:
            amount_memory = int(sys.argv[1])
        except:
            print("La cantidad de memoria debe ser un entero positivo.")
        cliente = Client(amount_memory)
        cliente.client()