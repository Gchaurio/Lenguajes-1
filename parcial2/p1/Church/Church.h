#ifndef CHURCH_H
#define CHURCH_H

#include <iostream>

/* Definiendo la clase Church */
class Church {

// Constructor que recibe dos parámetros: un entero 'n' y un puntero a un objeto Church 'other'
public:
  Church(int n, Church* other);

// Constructor que recibe un parámetro: un entero 'n'
  Church(int n);

// Destructor de la clase Church
  ~Church();

// Operador de suma sobrecargado para sumar dos objetos Church
  Church* operator+(const Church& other) const;

// Operador de multiplicación sobrecargado para multiplicar dos objetos Church
  Church* operator*(const Church& other) const;

// Método para obtener el valor de 'val'
  Church* getVal() const;

// Método para obtener el valor de 'n'
  int getN() const;

// Operador de salida sobrecargado para imprimir objetos Church
  friend std::ostream& operator<<(std::ostream& os, const Church& dt);

// Método para verificar si el objeto Church es 'Zero'
  bool isZero();

private:
  // Atributo privado que representa el valor de 'n'
  int n = 0;

  // Atributo privado que apunta a un objeto Church 'val'
  Church* val = nullptr;
};

#endif