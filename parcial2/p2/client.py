from exp_parser import Parser

# Cliente que maneja el programa.
class Client(object):

    def __init__(self):

        print('Manejador de expresiones aritmeticas - Gabriel Chaurio 17-10126\n')
        print('Inputs posibles:\nEVAL <orden> <expr>\nMOSTRAR <orden> <expr>\nSALIR\n')

    def client(self):
        while True:
            action = input("\nIntroduzca un comando:\n").strip().split(' ')
            if "EVAL" in action:
                if action[1] == ("PRE") or action[1] ==("POST") :
                    parser = Parser(action[1],action[2:len(action)])
                    print(parser.parse())
                else:
                    print("No se ha reconocido el orden")
            elif "MOSTRAR" in action:
                parser = Parser(action[1],action[2:len(action)])
                print(parser.mostrar())
            elif "SALIR" in action:
                exit()
            else:
                print("No se ha reconocido el comando")

if __name__ == '__main__':

    cliente = Client()
    cliente.client()