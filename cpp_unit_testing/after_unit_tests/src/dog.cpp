#include <iostream>
#include "dog.h"
Dog::Dog(const std::string &name, IToy &toy) : name(name), toy(toy) {}

void Dog::play() const {
  std::cout << name << ": Oh boy, oh boy! A toy!" << std::endl;
  toy.squeak();
  toy.getChewed();
  std::cout << name << ": BEST. DAY. EVER." << std::endl;
}

void Dog::display() const {
  std::cout << "Dog Name: " << name << std::endl;
  std::cout << name << " loves their toy: " << std::endl;
  toy.squeak();
}
