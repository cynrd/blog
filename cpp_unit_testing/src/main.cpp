#include "dog.h"
#include "toy.h"
int main() {
  Toy ball("Squeaky Ball");
  Dog buddy("Buddy", ball); // Pass the toy by reference

  buddy.display();
  buddy.play();

  return 0;
}
