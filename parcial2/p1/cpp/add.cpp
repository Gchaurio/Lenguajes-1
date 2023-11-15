#include "church.hpp"
#include <exception>

Church add(const Church& a, const Church& b) {
  switch (a.type) {
    case Church::Cero:
      return b;
    case Church::Suc:
      return Church(Suc(add(a.type, b.type)));
  }

  throw std::runtime_error("No se pudo realizar la suma");
}
