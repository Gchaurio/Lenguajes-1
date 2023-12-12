from VM import VM

def main():
    vm = VM()
    while True:
        user_input = input("\nComandos:\nCLASS <tipo> [<nombre>] o CLASS <tipo> : <superclase> [<nombre>] \nDESCRIBIR <tipo>\nSALIR\nIntroduzca su comando: ")
        if "CLASS" in user_input:
            parametros = user_input.strip().split(":")
            if len(parametros) == 2:
                clase = parametros[0].strip().split(" ")       
                clase = clase[1] 
                parametros = parametros[1].strip().split(" ")       
                if len(parametros) >= 2:
                    superClase = parametros[0]
                    metodos = parametros[1:]
                elif len(parametros) == 1:
                    superClase = parametros[0]
                    metodos = None
                else:
                    print(f'Error con los argumentos. \nEjemplo de uso: <tipo> [<nombre>] o <tipo> : <superclase> [<nombre>]')
            elif len(parametros) == 1 :
                parametros = parametros[0].split(" ")
                if parametros[1].strip() != '':
                    if len(parametros) >= 3:
                        clase = parametros[1]
                        superClase = None
                        metodos = parametros[2:]
                    else:
                        print(f'Error con los argumentos. \nEjemplo de uso: <tipo> [<nombre>] o <tipo> : <superclase> [<nombre>]')
                else:
                    print('Error con los argumentos. \nEjemplo de uso: <tipo> [<nombre>] o <tipo> : <superclase> [<nombre>]')
                        
            #print(clase, superClase, metodos)
            print(vm.define_class(clase, superClase, metodos))      

        elif "DESCRIBIR" in user_input:
            clase = user_input.strip().split(" ")
            print(vm.describir(clase[1]))

        elif user_input == "SALIR":
            exit()

        else:
            print("Acción no reconocida")

if __name__ == "__main__":
    main()