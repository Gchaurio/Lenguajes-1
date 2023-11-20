from manejador import Manejador

# Cliente que maneja el programa.
class Client(object):

    def __init__(self):

        self.manejador = Manejador()
        print('Inputs posibles:\nATOMICO <nombre> <representación> <alineación>\nSTRUCT <nombre> [<tipo>]\nUNION <nombre> [<tipo>]\nDESCRIBIR <nombre>\nSALIR\n')

    def client(self):

        while True:
            action = input("\nIntroduzca un comando:\n").strip().split(' ')

            # Verificamos el comando

            if action[0] == "ATOMICO":
                self.manejador.handle_atomico(action)
            elif action[0] == "STRUCT":
                self.manejador.handle_struct(action)
            elif action[0] == "UNION":
                self.manejador.handle_union(action)
            elif action[0] == "DESCRIBIR":
                self.manejador.describir(action[1])
            elif action[0] == "SALIR":
                exit()
            else:
                print("Error: Comando no reconocido")

if __name__ == '__main__':

    print("Manejador de tipo de datos. Gabriel Chaurio 17-10126")
    cliente = Client()
    cliente.client()