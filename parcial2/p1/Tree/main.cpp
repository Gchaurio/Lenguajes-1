#include <iostream>
#include <algorithm>
#include <string>

// Constructor del arbol
struct Arbol {
  int valor;
  Arbol *izq;
  Arbol *der;
};

// Funcion que crea un string con el arbol en posrder
std::string posOrder(Arbol *arbol)
{
    std::string  ans = "";
    if( arbol->izq != nullptr){
        ans += posOrder(arbol->izq);
    }
    if( arbol->der != nullptr){
        ans += posOrder(arbol->der);
    }
    ans += std::to_string(arbol->valor) + " ";
    return ans;
}

// Funcion que crea un string con el arbol en preorder
std::string preOrder(Arbol *arbol)
{
    std::string ans = std::to_string(arbol->valor) + " ";
    if( arbol->izq != nullptr){
        ans += preOrder(arbol->izq);
    }
    if( arbol->der != nullptr){
        ans += preOrder(arbol->der);
    }
    return ans;
}

// Funcion que chequea si el arbol es un max heap
bool esMaxHeap(Arbol *arbol) {
    if (arbol->izq == nullptr && arbol->der == nullptr) {
        return true;
    }

    return ((arbol->izq == nullptr || esMaxHeap(arbol->izq)) && (arbol->der == nullptr || esMaxHeap(arbol->der)) && (arbol->valor >= arbol->izq->valor) && (arbol->valor >=arbol->der->valor));
}

// Funcion que chequea si el arbol es simertrico, usando las funciones definidas anteriormente y comparando la salida.
bool esSimetrico(Arbol *arbol) {
  if (arbol->izq == nullptr && arbol->der == nullptr) {
    return true;
  }

    std::string str_preOrder = preOrder(arbol);
    std::string str_posOrder = posOrder(arbol);

  return (str_preOrder == str_posOrder);
}



int main() {

  // Crea un arbol simetrico max heap
  Arbol *arbol = new Arbol;
  arbol->valor = 5;
  arbol->izq = new Arbol;
  arbol->izq->valor = 5;
  arbol->izq->izq = new Arbol;
  arbol->izq->izq->valor = 5;
  arbol->izq->der = new Arbol;
  arbol->izq->der->valor = 5;
  arbol->der = new Arbol;
  arbol->der->valor = 5;
  arbol->der->izq = new Arbol;
  arbol->der->izq->valor = 5;
  arbol->der->der = new Arbol;
  arbol->der->der->valor = 5;

  // Chequea que efectivamente es un arbol simetrico max heap
  bool isSymmetricMaxHeap = esMaxHeap(arbol);
  bool isSymetric = esSimetrico(arbol);

  if (isSymmetricMaxHeap && isSymetric) {
    std::cout << "El arbol es un arbol max heap simetrico." << std::endl;
  } else {
    std::cout << "El arbol NO es un arbol max heap simetrico." << std::endl;
  }

  // Borramos el arbol de prueba
  delete arbol;


  // Create un arbol NO SIMETRICO max heap
  Arbol *arbol = new Arbol;
  arbol->valor = 5;
  arbol->izq = new Arbol;
  arbol->izq->valor = 5;
  arbol->izq->izq = new Arbol;
  arbol->izq->izq->valor = 4;
  arbol->izq->der = new Arbol;
  arbol->izq->der->valor = 3;
  arbol->der = new Arbol;
  arbol->der->valor = 5;
  arbol->der->izq = new Arbol;
  arbol->der->izq->valor = 2;
  arbol->der->der = new Arbol;
  arbol->der->der->valor = 1;

  // Chequea que efectivamente NO es un arbol simetrico max heap
  bool isSymmetricMaxHeap = esMaxHeap(arbol);
  bool isSymetric = esSimetrico(arbol);

  if (isSymmetricMaxHeap && isSymetric) {
    std::cout << "El arbol es un arbol max heap simetrico." << std::endl;
  } else {
    std::cout << "El arbol NO es un arbol max heap simetrico." << std::endl;
  }
  delete arbol;

  return 0;
}