from Manejador import Manejador

def main():
    manejador = Manejador()
    while True:
        user_input = input("\nComandos:\nCLASS <tipo> [<nombre>] o CLASS <tipo> : <Super Clase> [<nombre>] \nDESCRIBIR <tipo>\nSALIR\nIntroduzca su comando: ")
        if "CLASS" in user_input:
            args = user_input.strip().split(":")
            if len(args) == 2:
                clase = args[0].strip().split(" ")       
                clase = clase[1] 
                args = args[1].strip().split(" ")       
                if len(args) >= 2:
                    super = args[0]
                    metodos = args[1:]
                elif len(args) == 1:
                    super = args[0]
                    metodos = None
                else:
                    print(f'Error con los argumentos. \nEjemplo de uso: <tipo> [<nombre>] o <tipo> : <Super Clase> [<nombre>]')
            elif len(args) == 1 :
                args = args[0].split(" ")
                if args[1].strip() != '':
                    if len(args) >= 3:
                        clase = args[1]
                        super = None
                        metodos = args[2:]
                    else:
                        print(f'Error con los argumentos. \nEjemplo de uso: <tipo> [<nombre>] o <tipo> : <Super Clase> [<nombre>]')
                else:
                    print('Error con los argumentos. \nEjemplo de uso: <tipo> [<nombre>] o <tipo> : <Super Clase> [<nombre>]')
                        
            #print(clase, super, metodos)
            print(manejador.def_clase(clase, super, metodos))      

        elif "DESCRIBIR" in user_input:
            clase = user_input.strip().split(" ")
            print(manejador.describir(clase[1]))
        elif user_input == "SALIR":
            exit()
        else:
            print("Accion no reconocida")

if __name__ == "__main__":
    main()