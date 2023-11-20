from funciones import *
import time
import pandas as pd

def main(): 
    ns = [n for n in range(0, 250, 10)]    
    df = pd.DataFrame(columns=['Numero', 'Tiempo Recursion', 'Tiempo Recursion de Cola', 'Tiempo Iterativo'])

    for n in ns:

        print(n)

        start = time.time()
        n_recur = f_recur(n)
        time_recur = round(time.time() - start, 12)

        start = time.time()
        n_cola = f_cola(n)
        time_cola= round(time.time() - start, 12)

        start = time.time()
        n_iter = f_iter(n)
        time_iter = round(time.time() - start, 12)


        print(f"n_recur = {n_recur}")
        print(f"n_cola = {n_cola}")
        print(f"n_iter = {n_iter}")
        
    
        curr_df = pd.DataFrame(data={
            'Numero': [n],
            'Tiempo Recursion': time_recur,
            'Tiempo Recursion de Cola': time_cola,
            'Tiempo Iterativo': time_iter
        })

        df = pd.concat([df, curr_df], ignore_index=True)

    df.to_csv('results.csv', index=False)
    
if __name__=="__main__":
    main()