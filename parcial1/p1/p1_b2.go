package main

// Importamos los modulos necesarios
import (
    "bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Definimos el main
func main() {
    // Leemos el primer argumento, que es el nombre del archivo de texto.
	filename := os.Args[1]
	file, err := os.Open(filename)

	// Devolvemos error en caso de no ser un archivo correcto.
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()

	// Creamos un scanner que lea el archivo
	scanner := bufio.NewScanner(file)

	// Leemos el tamano de la matriz, ademas de crear un arreglo que almacene cada linea.
	n := 0
	var lines []string
	for scanner.Scan() {
		lines = append(lines,scanner.Text())
		n++
	}

	// Creamos una matriz cuadrada dummy del tamano de la matriz leida
	matrix := make([][]int, n)
	for i := 0; i < n; i++ {
		matrix[i] = make([]int, n)
	}

	// Leemos cada linea y aplicamos una funcion para convertir los strings en enteros
	for i := 0; i < n; i++ {
		ints := splitStringToInts(lines[i],n)
		for j := 0; j < n; j++ {
			matrix[i][j] = ints[j]
		}
	}

	// Verificamos que sea una matriz cuadrada
	if n != len(matrix[0]) {
		fmt.Println("La matriz no es cuadrada")
		return
	}

	// Imprimimos la matriz original
	fmt.Println("Matriz Original: \n")
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			fmt.Print(matrix[i][j], " ")
		}
		fmt.Println()
	}

    // Calculamos la transpuesta.
    matrixT := transpose(matrix)

    // Calculamos el producto matriz × matrizT.
    result := multiply(matrix, matrixT)

    // Imprimimos el resultado.
    fmt.Println("\nMatriz Resultante: \n")
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			fmt.Print(result[i][j], " ")
		}
		fmt.Println()
	}
}

// Separa una linea de string y la convierte en un arreglo de enteros
func splitStringToInts(s string, n int) []int {
	// Separa la linea de strings en strings individuales
    ints := strings.Split(s, " ")

	// De haber mas caracteres que lineas, se devuelve error
	if len(ints) != n{
		fmt.Println("La matriz no es cuadrada")
    	os.Exit(1)
	}
    // Convierte los string a enteros
    var intInts []int
    for _, strInt := range ints {
        int, err := strconv.Atoi(strInt)
        if err != nil {
            fmt.Println("Todos los caracteres del archivo tienen que ser enteros")
        	os.Exit(1)
        }
        intInts = append(intInts, int)
    }

    return intInts
}

func transpose(A [][]int) [][]int {
    // Declaramos una matriz cuadrada de la misma dimensión que A.
    AT := make([][]int, len(A))
    for i := 0; i < len(A); i++ {
        AT[i] = make([]int, len(A[0]))
    }

    // Calculamos la transpuesta de A.
    for i := 0; i < len(A); i++ {
        for j := 0; j < len(A[0]); j++ {
            AT[j][i] = A[i][j]
        }
    }

    return AT
}

func multiply(A [][]int, AT [][]int) [][]int {
    // Declaramos una matriz cuadrada de la misma dimensión que A.
    B := make([][]int, len(A))
    for i := 0; i < len(A); i++ {
        B[i] = make([]int, len(A[0]))
    }

    // Calculamos el producto A × AT.
    for i := 0; i < len(A); i++ {
        for j := 0; j < len(A[0]); j++ {
            for k := 0; k < len(A); k++ {
                B[i][j] += A[i][k] * AT[k][j]
            }
        }
    }

    return B
}