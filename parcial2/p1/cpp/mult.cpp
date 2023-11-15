#include "church.hpp"
#include <exception>

Church multiply(const Church& a, const Church& b) {
  switch (a.type) {
    case Church::Cero:
      return Church::Cero;
    case Church::Suc:
      return add(multiply(a.type, b), b);
  }

  throw std::runtime_error("No se pudo realizar la multiplicación");
}