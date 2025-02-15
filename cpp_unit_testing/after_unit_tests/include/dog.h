#ifndef DOG__H
#define DOG__H
#include <string>
#include "toy.h"

class Dog {
private:
  std::string name;
  IToy &toy;

public:
  Dog(const std::string &name, IToy &toy);
  void play() const;
  void display() const;
};

#endif // DOG__H
