#include <iostream>
#include "toy.h"
Toy::Toy(const std::string &name) : name(name) {}

void Toy::squeak() const {
  std::cout << "Toy (" << name << "): *Squeak squeak!*" << std::endl;
}

void Toy::getChewed() const {
  std::cout << "Toy (" << name << "): Why do you always chew on me?!"
            << std::endl;
}
