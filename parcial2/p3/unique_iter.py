import sys
import ast

def unique_crescend(lista):
    
    returned = [str([])]

    for i in range (0,len(lista)):
        lista[i] = int(lista[i])


    for i in range(len(lista)):

        sublista = [lista[i]]

        returned.append(str(sublista))

        for j in range(i + 1, len(lista)):

            for k in range(j, len(lista)):

                if lista[k] > sublista[-1]:

                    sublista.append(lista[k])
                    returned.append(str(sublista))
                
            sublista = [lista[i]]

    uniques =  []
    [uniques.append(x) for x in returned if x not in uniques]

    for i in range (0,len(uniques)):

        uniques[i] = ast.literal_eval(uniques[i])
        
        yield uniques[i]

if __name__ == "__main__":

    lista = list(sys.argv[1:len(sys.argv)])
    for sublista in unique_crescend(lista):
        print(sublista)