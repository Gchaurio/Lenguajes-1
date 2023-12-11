import re
from VM import VM

def main():
    vm = VM()
    while True:
        user_input = input("Comandos: CLASS <tipo> [<nombre>] o CLASS <tipo> : <superclase> [<nombre>] \nDESCRIBIR <tipo>\nSALIR\n")
        if "CLASS" in user_input:

            parametros = re.sub(r'^CLASS', '', user_input).strip().split(":")
            if len(parametros) == 2:
                clase = parametros[0].strip()         
                parametros = parametros[1].split()            
                if len(parametros) >= 2:
                    superClase = parametros[0]
                    metodos = parametros[1:]
                else:
                    print(f'Error en accion: "{user_input}"\nSe requieren los argumentos'
                    ' <tipo> [<nombre>] o <tipo> : <superclase> [<nombre>]')
                    return
            elif len(parametros) == 1 and parametros[0].strip() != '':
                parametros = parametros[0].split()
                if len(parametros) >= 2:
                    clase = parametros[0]
                    superClase = None
                    metodos = parametros[1:]
                else:
                    print(f'Error en accion: "{user_input}"\nSe requieren los argumentos'
                    ' <tipo> [<nombre>] o <tipo> : <superclase> [<nombre>]')
                    return
            else:
                print(f'Error en accion: "{user_input}"\nSe requieren los argumentos'
                    ' <tipo> [<nombre>] o <tipo> : <superclase> [<nombre>]')
                return
            
            vm.define_class(clase, superClase, metodos)        

        elif "DESCRIBIR" in user_input:
            clase = re.sub(r'^DESCRIBIR', '', user_input).strip()
            vm.describir(clase)

        elif user_input == "SALIR":
            exit()

        else:
            print("Acción no reconocida")

if __name__ == "__main__":
    main()