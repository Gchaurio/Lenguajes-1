#include "Church.h"

/* Constructor de la clase Church */
Church::Church(int n, Church* other) {
  // Verifica que el parámetro 'n' sea positivo
  try {
    if (n < 0) {
      throw std::invalid_argument("La entrada debe ser positiva");
    }

    // Si se recibe un objeto Church como parámetro, verifica que sea del tipo correcto
    if (other != nullptr) {
      if (typeid(*other) != typeid(Church)) {
        throw std::invalid_argument("La entrada debe ser de tipo Church también");
      }

      // Establece el valor de 'val' y 'n' en base al objeto Church recibido
      val = other;
      this->n = other->n + 1;
    } else {
      // Establece el valor de 'n' y 'val' en base al parámetro 'n'
      this->n = n;
      val = nullptr;
      if (n > 0) {
        val = new Church(n - 1); // Crea un nuevo objeto Church si 'n' es mayor a 0
      }
    }
  } catch (const std::invalid_argument& e) {
    // Maneja la excepción lanzada en caso de error de parámetro
    std::cerr << e.what() << std::endl;
    throw;
  }
}

/* Constructor de la clase Church que recibe un parámetro 'k' */
Church::Church(int k) {
  // Establece el valor de 'n' y 'val' en base al parámetro 'k'
  if (k == 0) {
    n = 0;
    val = NULL;
  } else {
    n = k;
    val = new Church(k - 1); // Crea un nuevo objeto Church si 'k' es mayor a 0
  }
}

/* Destructor de la clase Church */
Church::~Church() {
  // Destruye el objeto Church apuntado por 'val'
  if (val) {
    delete val;
  }
}

/* Operador de suma para la clase Church */
Church* Church::operator+(const Church& other) const {
  // Suma los valores de 'n' de los dos objetos Church
  int k = other.n + this->n;
  return new Church(k); // Crea un nuevo objeto Church con el resultado de la suma
}

/* Operador de multiplicación para la clase Church */
Church* Church::operator*(const Church& other) const {
  // Multiplica los valores de 'n' de los dos objetos Church
  int k = other.n * this->n;
  return new Church(k); // Crea un nuevo objeto Church con el resultado de la multiplicación
}

/* Método para obtener el valor de 'val' */
Church* Church::getVal() const {
  return val;
}

/* Método para obtener el valor de 'n' */
int Church::getN() const {
  return n;
}

/* Método para verificar si el objeto Church es 'Zero' */
bool Church::isZero() {
  return !val; // Retorna verdadero si 'val' es nulo, indicando que el objeto es 'Zero'
}

/* Sobrecarga del operador de salida para imprimir objetos Church */
std::ostream& operator<<(std::ostream& os, const Church& c) {
  Church ch = c; // Crea una copia del objeto Church para evitar modificaciones al original

  // Muestra el valor de 'val' o el mensaje "Zero" según corresponda
  if (!ch.getVal()) {
    os << "Zero";
  } else {
    Church *val = ch.getVal(); // Obtiene el valor de 'val'
    os << "Suc(" << *val << ")"; // Muestra el valor de 'val' entre paréntesis
  }

  return os; // Retorna la referencia al flujo de salida
}