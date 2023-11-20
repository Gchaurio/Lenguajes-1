#include "Church.h"
#include <iostream>

int main(int argc, char* argv[]) {
    Church a(2);
    Church b(3);

    Church* sum = a + b;
    Church* product = a * b;

    std::cout << b << std::endl;
    std::cout << "Sum: " << sum->getN() << std::endl;
    std::cout << "Product: " << product->getN() << std::endl;

    return 0;
}