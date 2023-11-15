import sys

def unique_crescend(lista):
    
    yield []

    for i in range(len(lista)):


        sublista = [lista[i]]

        yield sublista
        for j in range(i + 1, len(lista)):


            for k in range(j, len(lista)):

                if lista[k] > sublista[-1]:
                    sublista.append(lista[k])
                    yield sublista
                
            sublista = [lista[i]]


if __name__ == "__main__":
    lista = list(sys.argv[1:len(sys.argv)])
    for sublista in unique_crescend(lista):
        print(sublista)