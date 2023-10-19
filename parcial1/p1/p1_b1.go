package main

// Importo los paquetes necesarios
import (
    "fmt"
    "os"
    "strings"
    "strconv"
)

// Defino el main
func main() {

	// Recibo argumentos desde consola, si son menos o mas que 3, se imprime un instructivo para usar el codigo.
    if len(os.Args) != 3 {
        fmt.Println("Usage: p1_b1.go <string> <n>")
        os.Exit(1)
    }

	// Se lee el argumento en la posicion 1, el cual sera el string a rotar (se asigna a s).
    s := os.Args[1]

	// Se asigna al segundo argumento al numero de veces a ser rotados (se asigna a n). 
    n, err := strconv.Atoi(os.Args[2])

	// Se revisa que el input sea un entero, de no ser asi se lanza error y se cancela la ejecucion.
    if err != nil {
        fmt.Println("Error: n must be an integer.")
        os.Exit(1)
    }

	// Si el numero de veces a rotar es mayor al tamano del string, se calcula el equivalente dentro del rango del largo del string.
    if n > len(s) {
        n = n % len(s)
    }

	// Se llama a la funcion rotar y se imprime el resultado
    fmt.Println(rotar(s, n))
}

// Se define la funcion que rotara el string. Esta recibe un string y el numero de veces a ser rotado.
// Se aplica split para separar todas las letras y se pega el slice original al final de la cadena
// posteriormente se juntan los slices
func rotar(s string, n int) string {
    slice := strings.Split(s, "")
    slice = append(slice[n:], slice[:n]...)
    return strings.Join(slice, "")
}