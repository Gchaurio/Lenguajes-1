# Cliente que maneja el programa.
class Client(object):

    def __init__(self):

        self.buddy_system = Buddy_System(blocks)
        print('Inputs posibles:\nATOMICO <nombre> <representación> <alineación>\nLIBERAR <nombre>\nMOSTRAR\nSALIR\n')

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

    print("Manejador de tipo de datos. Gabriel Chaurio 17-10126")
    cliente = Client()
    cliente.client()